
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Qurban Mohebi
-- Create date: 28-02-2024
-- Description:	stored procedure to be used for checking out equpment library assets
-- =============================================

CREATE PROCEDURE library_checkout 
	@EquipmentId VARCHAR(50), 
	@LocationId VARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE @LoanStatus VARCHAR(50)
	SELECT @LoanStatus = EquipmentLibraryStatusId 
	FROM Equipment
	WHERE EquipmentId = @EquipmentId

	IF @LoanStatus = 'WWW3'
	BEGIN



	--get next loan code
	DECLARE @NewCode VARCHAR(50)
	EXEC dbo.qNextCode @EntityType = 34, @Code = @NewCode output

	-- Get the loan status
	DECLARE @LoanStatusId VARCHAR(50)
	SELECT TOP 1 @LoanStatusId = LoanStatusId 
	FROM LoanStatus
	WHERE LoanStatusClassId = 'INPROGRESS'
	ORDER BY LoanStatusCode

	DECLARE @SiteId VARCHAR(50)
	DECLARE @SiteShortName VARCHAR(255)
	DECLARE @LocationShortName VARCHAR(255)

	SELECT @LocationShortName = LocationShortName, @SiteShortName = SiteShortName, @SiteId = Location.SiteId	 
	FROM Location 
		INNER JOIN [Site]
			ON Location.SiteId = [Site].SiteId
	WHERE LocationId = @LocationId

		-- Create the loan
	DECLARE @LoanId VARCHAR(50) = NEWID()
	DECLARE @Notes VARCHAR(50) = 'Created by library checkout'

	INSERT INTO Loan
		(LoanId, LoanCode, LoanStatusId, EquipmentId, LocationId, SiteId, StartDate, OutOfHours, LoanNotes)
	VALUES
		(@LoanId, @NewCode, @LoanStatusId, @EquipmentId, @LocationId, @SiteId, GETDATE(), 1, @Notes)

		--
	-- Update the equipment record
	UPDATE Equipment
	SET EquipmentLibraryStatusId = 'WWW3', ModificationDate = GETDATE()
	WHERE EquipmentId = @EquipmentId

	--
	-- Update the equipment location history
	INSERT INTO EquipmentLocationHistory
		(EquipmentLocationHistoryId, EquipmentId, LocationId, LocationShortName, SiteShortName, ArrivalDate, HistoryOrigin)
	VALUES 
		(NEWID(), @EquipmentId, @LocationId, @LocationShortName, @SiteShortName, GETDATE(), 'library check out')

END
GO
