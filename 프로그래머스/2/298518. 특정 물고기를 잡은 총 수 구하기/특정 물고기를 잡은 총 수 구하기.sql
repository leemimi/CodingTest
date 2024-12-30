SELECT COUNT(*)AS FISH_COUNT
FROM FISH_INFO as A left join fish_name_info as b on a.fish_type = b.fish_type
WHERE b.fish_name = 'BASS' or b.fish_name = 'SNAPPER'

