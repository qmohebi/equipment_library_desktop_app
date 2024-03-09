GO
/****** Object:  StoredProcedure [dbo].[LibraryGetAsset]    Script Date: 09/03/2024 04:06:17 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Qurban Mohebi
-- Create date: 01-03-2024
-- Description:	
-- =============================================
CREATE PROCEDURE [dbo].[LibraryGetAsset] 
	-- Add the parameters for the stored procedure here
	@EquipmentCode VARCHAR(50)

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
select 
	e.EquipmentId
	,c.CategoryShortName
	,e.EquipmentLibraryStatusId
	,l.LoanStatusId
	,lc.LocationShortName as LoanLocation
from 
	Equipment e
left JOIN 
	Loan l ON l.EquipmentId = e.EquipmentId
left join 
	Location lc on lc.LocationId = l.LocationId
left join 
	Category c on c.CategoryId = e.CategoryId
where 
	EquipmentCode = @EquipmentCode AND e.Inactive= 0
ORDER by 
	l.LoanStatusId

END
