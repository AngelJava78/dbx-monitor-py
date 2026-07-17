SELECT
    s.subprocess_id,
    s.subprocess_name
FROM
    public.subprocesses s
ORDER BY
    s.subprocess_id;