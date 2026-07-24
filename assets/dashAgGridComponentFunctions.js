var dagcomponentfuncs =
    (window.dashAgGridComponentFunctions =
        window.dashAgGridComponentFunctions || {});


function createDatabricksLink(value, url) {
    if (value === null || value === undefined) {
        return null;
    }

    if (!url) {
        return React.createElement(
            "span",
            null,
            String(value)
        );
    }

    return React.createElement(
        "a",
        {
            href: String(url),
            target: "_blank",
            rel: "noopener noreferrer",
            onClick: function (event) {
                event.stopPropagation();
            },
            style: {
                color: "#0563C1",
                textDecoration: "underline",
                cursor: "pointer"
            }
        },
        String(value)
    );
}


dagcomponentfuncs.RunDurationLink = function (props) {
    var runPageUrl =
        props.data && props.data.run_page_url
            ? String(props.data.run_page_url)
            : null;

    if (!runPageUrl) {
        return createDatabricksLink(props.value, null);
    }

    try {
        var parsedUrl = new URL(runPageUrl);

        // Obtiene el workspace ID desde ?o=...
        var workspaceId = parsedUrl.searchParams.get("o");

        // Ejemplo del hash:
        // #job/120783322819248/run/280770854805881
        var hashMatch = parsedUrl.hash.match(
            /^#job\/(\d+)\/run\/(\d+)$/
        );

        if (!workspaceId || !hashMatch) {
            console.warn(
                "Unable to transform Databricks run URL:",
                runPageUrl
            );

            return createDatabricksLink(
                props.value,
                runPageUrl
            );
        }

        var jobId = hashMatch[1];
        var runId = hashMatch[2];

        var timelineUrl =
            parsedUrl.origin +
            "/jobs/" +
            encodeURIComponent(jobId) +
            "/runs/" +
            encodeURIComponent(runId) +
            "?o=" +
            encodeURIComponent(workspaceId) +
            "&view=timeline";

        return createDatabricksLink(
            props.value,
            timelineUrl
        );
    } catch (error) {
        console.error(
            "Failed to build Databricks timeline URL:",
            error
        );

        return createDatabricksLink(
            props.value,
            runPageUrl
        );
    }
};


dagcomponentfuncs.DatabricksJobLink = function (props) {
    var jobId = props.value;

    var runPageUrl =
        props.data && props.data.run_page_url
            ? String(props.data.run_page_url)
            : null;

    if (
        jobId === null ||
        jobId === undefined ||
        !runPageUrl
    ) {
        return createDatabricksLink(jobId, null);
    }

    try {
        var parsedUrl = new URL(runPageUrl);

        // Obtiene el workspace ID desde ?o=...
        var workspaceId = parsedUrl.searchParams.get("o");

        if (!workspaceId) {
            console.warn(
                "Workspace ID was not found in Databricks URL:",
                runPageUrl
            );

            return createDatabricksLink(
                jobId,
                runPageUrl
            );
        }

        var jobPageUrl =
            parsedUrl.origin +
            "/jobs/" +
            encodeURIComponent(jobId) +
            "/tasks?o=" +
            encodeURIComponent(workspaceId);

        return createDatabricksLink(
            jobId,
            jobPageUrl
        );
    } catch (error) {
        console.error(
            "Failed to build Databricks job URL:",
            error
        );

        return createDatabricksLink(
            jobId,
            runPageUrl
        );
    }
};

dagcomponentfuncs.TaskRunLink = function (props) {
    var taskRunId = props.value;

    var runPageUrl =
        props.data && props.data.run_page_url
            ? String(props.data.run_page_url)
            : null;

    if (
        taskRunId === null ||
        taskRunId === undefined ||
        !runPageUrl
    ) {
        return createDatabricksLink(taskRunId, null);
    }

    try {
        var parsedUrl = new URL(runPageUrl);
        var workspaceId = parsedUrl.searchParams.get("o");

        if (!workspaceId) {
            return createDatabricksLink(
                taskRunId,
                runPageUrl
            );
        }

        var taskRunUrl =
            parsedUrl.origin +
            "/jobs/runs/" +
            encodeURIComponent(taskRunId) +
            "?o=" +
            encodeURIComponent(workspaceId);

        return createDatabricksLink(
            taskRunId,
            taskRunUrl
        );
    } catch (error) {
        console.error(
            "Failed to build Databricks task run URL:",
            error
        );

        return createDatabricksLink(
            taskRunId,
            runPageUrl
        );
    }
};