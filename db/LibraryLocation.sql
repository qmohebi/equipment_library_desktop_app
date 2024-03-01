
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Qurban Mohebi
-- Create date: 01-03-2024
-- Description:	Populate loan location for equipment library check out
-- show only location that belongs to SGH and active
-- =============================================
CREATE PROCEDURE LibraryLocation 

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	SELECT 
		Location.LocationShortName, 
		Location.LocationId 
	FROM 
		Location
	JOIN Site ON Location.SiteId = site.SiteId
	WHERE Location.Inactive = 0 and location.SiteId = 'STG200404040007'
	for json auto

END
GO
