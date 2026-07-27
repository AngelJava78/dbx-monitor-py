SELECT
    ts.scenario_id,
    ts.description AS scenario_description,
    ss.scenario_subprocess_id,
    ss.execution_order,
    s.subprocess_id,
    s.subprocess_name,
    tr.run_id AS test_run_id,
    tr.executed_at,
    tr.folio,
    r.job_id,
    r.job_name,
    r.run_id,
    r.started_cdmx,
    r.ended_cdmx,
    TO_CHAR(r.duration, 'HH24:MI:SS') AS duration,
    r.run_page_url,
    r.run_type,
    r.result_state,
    r.process_id,
    r.stage_id,
    r.substage_id,
    st.substage_name,
    r.username,
    r.folio_number,
    r.parameter_source
FROM public.test_scenarios ts
INNER JOIN public.scenario_subprocess ss
    ON ss.scenario_id = ts.scenario_id
INNER JOIN public.subprocesses s
    ON s.subprocess_id = ss.subprocess_id
INNER JOIN public.test_runs tr
    ON tr.scenario_subprocess_id = ss.scenario_subprocess_id
INNER JOIN public.runs r
    ON r.folio_number = tr.folio
INNER JOIN public.substages st
    ON st.substage_id = r.substage_id
WHERE tr.executed_at >= %(start_date)s
  AND tr.executed_at < %(end_date)s
  and COALESCE(r.folio_number, '') <> '' 
  AND (
      %(scenario_id)s = 0
      OR ts.scenario_id = %(scenario_id)s
  )
  AND (
      %(subprocess_id)s = 0
      OR s.subprocess_id = %(subprocess_id)s
  )
  AND (
      %(folio)s IS NULL
      OR tr.folio ILIKE %(folio)s
  )
ORDER BY
    ts.scenario_id,
    ss.execution_order,
    s.subprocess_id,
    tr.executed_at,
    tr.folio,
    r.started_cdmx;