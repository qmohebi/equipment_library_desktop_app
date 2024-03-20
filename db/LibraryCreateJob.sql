USE [TRIAL_DB_TEST_DB]
GO
/****** Object:  StoredProcedure [dbo].[US_CreateJob]    Script Date: 14/03/2024 14:34:02 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Qurban Mohebi
-- Create date: 2024-01-24
-- Description:	Updating of loan and library status on loan equipment and 
--Creation of job by Library chekout APP
-- =============================================

CREATE PROCEDURE LibraryCreateJob
	@JobTypeId NVARCHAR(50),
	@JobStatusId NVARCHAR(50),
	@EquipmentId NVARCHAR(50),
	@ReportedFault TEXT,	
	@WorkEndDate DATETIME,
	@TechnicianId NVARCHAR(50),
	@WorkDone TEXT,
	@UserId NVARCHAR(50),
	@TestEquipmentId NVARCHAR(50) = NULL,
	@TestEquipmentId2 NVARCHAR(50) = NULL,
	@AssistantId NVARCHAR (50) = Null,
	@VisualInspection Bit = 0,
	@ElectricalSafetyTest bit = 0,
	@FunctionCheck bit = 0,
	@BatteryReplaced bit = 0,
	@BatteryChecked bit = 0,
	@CreateJob bit = 0

AS
BEGIN

	-- Get the next Job No
	DECLARE @JobCode NVARCHAR(50)
	EXEC qNextCode 17, @JobCode OUTPUT
	
	--
	-- Pad the job number
	DECLARE @JobSort VARCHAR(50)
	IF ISNUMERIC(LTRIM(RTRIM(@JobCode))) != 0
	BEGIN
		SELECT 	@JobSort = SPACE( 50 - LEN(LTRIM(RTRIM(@JobCode)))) + LTRIM(RTRIM(@JobCode))
	END

	-- some fields that is needed for job but can be auto populated:
	DECLARE @JobPriorityId NVARCHAR(50) = 'WWW4'
	DECLARE @TakenById NVARCHAR(50) = @TechnicianId

	-- If we have equipment then brand, model & category must come from that
	DECLARE @BrandId VARCHAR(50)
	DECLARE @ModelId VARCHAR(50)
	DECLARE @CategoryId VARCHAR(50)
	DECLARE @TeamId VARCHAR(50)
	DECLARE @JobId VARCHAR(50)
	DECLARE @JobDate DATETIME

	SET @BrandId = NULL
	SET @ModelId = NULL
	SET @CategoryId = NULL
	SET @TeamId = NULL
	SET @JobId = NEWID()
	SET @JobDate = GETDATE()

	IF @EquipmentId IS NOT NULL
	BEGIN
		SELECT @BrandId = BrandId, 
			@ModelId = ModelId, 
			@CategoryId = CategoryId,
			@TeamId = TeamId
		FROM Equipment
		WHERE EquipmentId = @EquipmentId
	END

	--
	-- Get the contract
	DECLARE @ContractId VARCHAR(50)
	SELECT @ContractId = dbo.CurrentContractId( @EquipmentId, @JobDate)

	--
	-- Get the customer contract
	DECLARE @CustomerContractId VARCHAR(50)
	SELECT @CustomerContractId = dbo.CurrentCustomerContractId( @EquipmentId, @JobDate)

	-- Update the loan to complete and make the library status to available
	BEGIN
		UPDATE 
			Loan
		SET
			LoanStatusId = 'STG2005061300003', 
			ReturnDate = GETDATE()
		WHERE 
			EquipmentId = @EquipmentId
			AND
			LoanStatusId != 'STG2005061300003'

		UPDATE 
			Equipment
		SET 
			EquipmentLibraryStatusId = 'WWW2', ModificationDate = GETDATE()
		WHERE 
			EquipmentId = @EquipmentId
	END

	-- if the job created flas is set to true, create job
	IF @CreateJob = 1
	BEGIN
		-- Create the job
		INSERT INTO Job
			(JobId, JobCode,  JobTypeId, JobStatusId, JobPriorityId, EquipmentId, CallDate,CreationDate, JobSort, ReportedFault,
			WorkStartDate, WorkEndDate, TechnicianId, AssistantId, WorkDone, BrandId, ModelId, CategoryId, ContractId, CustomerContractId, 
			TakenById, VisualInspection, EST, FunctionalCheck, BatteryReplaced, BatteryChecked)
		
		VALUES
			(@JobId, @JobCode, @JobTypeId, @JobStatusId, @JobPriorityId, @EquipmentId, @JobDate, @JobDate, @JobSort, @ReportedFault,
			GETDATE(), @WorkEndDate, @TechnicianId, @AssistantId, @WorkDone, @BrandId, @ModelId, @CategoryId, @ContractId, @CustomerContractId,
			@TakenById, @VisualInspection, @ElectricalSafetyTest, @FunctionCheck, @BatteryReplaced, @BatteryChecked)
	
		--
		-- Audit the job creation
		INSERT INTO CommonAudit
			( AuditId, AuditType, AuditDate, ChangedById, OriginalValue, NewValue, EntityId, AuditAction )
		VALUES ( NEWID(), 'JBC', @JobDate, @UserId, '', 'Job Created', @JobId, 'Insert' )

		--
		-- Audit the status
		IF @JobStatusId IS NOT NULL
		BEGIN
			DECLARE @AuditDesc2 VARCHAR(255)
			SELECT @AuditDesc2 = ISNULL(JobStatusShortName, '')
			FROM JobStatus
			WHERE JobStatusId = @JobStatusId

			INSERT INTO CommonAudit
				( AuditId, AuditType, AuditDate, ChangedById, OriginalValue, NewValue, EntityId, AuditAction )
			VALUES ( NEWID(), 'JST', GETDATE(), @UserId, NULL, @AuditDesc2, @JobId, 'Insert' )
		END

	END

END