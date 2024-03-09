-- findout loan status
SELECT 
    e.EquipmentId
    ,c.CategoryShortName
    ,e.EquipmentLibraryStatusId
	,ls.EquipmentLibraryStatusShortName
	,l.LoanStatusId
	,s.LoanStatusShortName
FROM 
    Equipment e
    JOIN Category c ON e.CategoryId = c.CategoryId
	JOIN EquipmentLibraryStatus ls ON e.EquipmentLibraryStatusId = ls.EquipmentLibraryStatusId
	JOIN Loan l ON l.EquipmentId = e.EquipmentId
	join LoanStatus s on s.LoanStatusId = l.LoanStatusId
WHERE 
    e.EquipmentCode = '5515996'
ORDER by l.LoanStatusId

select LoanStatusId, ReturnDate from Loan where EquipmentId = 'E7FE96E3-F553-4801-9A33-2F42C0B0D428'

-- update equipment if it is on loan and only update the in progress loans
-- update the asset to reflect the current library status of available
begin tran
update Loan
Set LoanStatusId = 'STG2005061300003', 
ReturnDate = GETDATE()
where EquipmentId = 'E7FE96E3-F553-4801-9A33-2F42C0B0D428'
and LoanStatusId != 'STG2005061300003'

	UPDATE Equipment
	SET EquipmentLibraryStatusId = 'WWW2', ModificationDate = GETDATE()
	WHERE EquipmentId = 'E7FE96E3-F553-4801-9A33-2F42C0B0D428' 
commit
rollback


