SELECT a.item_id, a.item_name
FROM ITEM_INFO A JOIN ITEM_TREE B ON A.ITEM_ID = B.ITEM_ID
where b.parent_item_id is null
order by a.item_id asc