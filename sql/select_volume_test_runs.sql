SELECT
    r.job_id,
    r.job_name,
    r.run_id,
    r.started_cdmx,
    r.ended_cdmx,
    TO_CHAR(r.duration, 'HH24:MI:SS') AS duration,
    r.run_page_url,
    r.run_type,
    r.result_state,
    r.termination_code,
    r.workspace_id,
    r.process_id,
    r.subprocess_id,
    sp.subprocess_name,
    r.stage_id,
    r.substage_id,
    ss.substage_name,
    r.username,
    r.folio_number,
    r.parameter_source,
    ts.scenario_id,
    ts.description AS scenario_description,
    ssp.expected_records AS production_records
FROM public.runs r
LEFT JOIN public.subprocesses sp
    ON sp.subprocess_id = r.subprocess_id
LEFT JOIN public.substages ss
    ON ss.substage_id = r.substage_id
LEFT JOIN public.test_runs tr
    ON tr.folio = r.folio_number
LEFT JOIN public.scenario_subprocess ssp
    ON ssp.scenario_subprocess_id = tr.scenario_subprocess_id
LEFT JOIN public.test_scenarios ts
    ON ts.scenario_id = ssp.scenario_id
WHERE r.started_cdmx >= %(start_date)s
  AND r.started_cdmx < %(end_date)s
  AND (
      %(scenario_id)s = 0
      OR ts.scenario_id = %(scenario_id)s
  )
  AND (
      %(folio)s IS NULL
      OR r.folio_number ILIKE %(folio)s
  )
ORDER BY r.started_cdmx;