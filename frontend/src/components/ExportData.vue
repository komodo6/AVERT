<template>
  <div>
    <q-btn-dropdown
      class="q-mx-sm"
      color="primary"
      icon-right="archive"
      label="Export to File"
      no-caps
    >
      <q-list>
        <q-item clickable v-close-popup @click="exportJSON">
          <q-item-section>
            <q-item-label>JSON</q-item-label>
          </q-item-section>
        </q-item>

        <q-item clickable v-close-popup @click="exportTable">
          <q-item-section>
            <q-item-label>CSV</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>
<script>
import { exportFile } from "quasar";
export default {
  props: {
      rowData: {},
      headers: {},
  },
  setup(props) {
    function wrapCsvValue(val, formatFn) {
      let formatted = formatFn !== void 0 ? formatFn(val) : val;

      formatted =
        formatted === void 0 || formatted === null ? "" : String(formatted);

      formatted = formatted.split('"').join('""');
      /**
       * Excel accepts \n and \r in strings, but some other CSV parsers do not
       * Uncomment the next two lines to escape new lines
       */
      // .split('\n').join('\\n')
      // .split('\r').join('\\r')

      return `"${formatted}"`;
    }
    const exportJSON = () => {
      console.log(props.rowData)
      let data = JSON.stringify(props.rowData, null, 2);

      const status = exportFile("data.json", data, "application/json");

      if (status !== true) {
        $q.notify({
          message: "Browser denied file download...",
          color: "negative",
          icon: "warning",
        });
      }
    };
    const exportTable = () => {
      console.log(props.rowData)
      // naive encoding to csv format
      const content = [props.headers.map((col) => wrapCsvValue(col.label))]
        .concat(
          props.rowData.map((row) =>
            props.headers
              .map((col) =>
                wrapCsvValue(
                  typeof col.field === "function"
                    ? col.field(row)
                    : row[col.field === void 0 ? col.name : col.field],
                  col.format
                )
              )
              .join(",")
          )
        )
        .join("\r\n");

      const status = exportFile("data.csv", content, "text/csv");

      if (status !== true) {
        $q.notify({
          message: "Browser denied file download...",
          color: "negative",
          icon: "warning",
        });
      }
    };

    return {
      exportTable,
      exportJSON,
    };
  },
};
</script>
<style></style>
