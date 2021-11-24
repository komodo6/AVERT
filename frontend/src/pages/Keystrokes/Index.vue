<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="Keystrokes"
          :columns="columns"
          :rows="rows"
          :filter="filter"
          selection="multiple"
          v-model:selected="selected"
          row-key="id"
        >
          <template v-slot:top-right>
            <q-input
              borderless
              dense
              debounce="300"
              v-model="filter"
              placeholder="Search"
            >
              <template v-slot:append>
                <q-icon name="search"> </q-icon>
              </template>
            </q-input>
            <ExportData :rowData="rows" :headers="columns" />
          </template>

          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td>
                <q-checkbox v-model="props.selected"> </q-checkbox>
              </q-td>
              <q-td key="timestamp" :props="props">
                {{ props.row.timestamp }}
              </q-td>
              <q-td key="ip_address" :props="props">
                {{ props.row.ip_address }}
              </q-td>
              <q-td key="mac_address" :props="props">
                {{ props.row.mac_address }}
              </q-td>
              <q-td key="key" :props="props">
                {{ props.row.key }}
              </q-td>
              <q-td key="annotations" :props="props">
                <div
                  v-for="annotation in props.row.annotations"
                  :key="annotation"
                >
                  {{ annotation }}
                </div>
              </q-td>
              <q-td key="tags" :props="props">
                <q-select
                  label="Tags"
                  filled
                  :v="props.row.tags"
                  v-model="props.row.tags"
                  @update:model-value="updateTags(props.row.tags, props.row.id)"
                  use-input
                  use-chips
                  multiple
                  hide-dropdown-icon
                  input-debounce="0"
                  new-value-mode="add"
                  style="width: 250px"
                />
              </q-td>
            </q-tr>
          </template>
        </q-table>
      </div>
    </div>
  </div>
</template>

<script>
const columns = [
  {
    name: "timestamp",
    label: "Date/Tme",
    field: "timestamp",
    sortable: true,
    align: "center",
  },
  {
    name: "ip_address",
    label: "IP Address",
    field: "ip_address",
    align: "center",
    sortable: true,
  },
  {
    name: "mac_address",
    label: "MAC Address",
    field: "mac_address",
    align: "center",
    sortable: true,
  },
  {
    name: "key",
    label: "Key",
    field: "key",
    align: "center",
    sortable: true,
  },
  {
    name: "annotations",
    label: "Annotations",
    name: "annotations",
    align: "center",
    sortable: false,
  },
  {
    name: "tags",
    label: "Tags",
    name: "tags",
    align: "center",
    sortable: false,
  },
];
import axios from "axios";
import { onMounted, ref } from "vue";
import { useQuasar } from "quasar";
import ExportData from "../../components/ExportData.vue";
import { fetchKeystrokes, updateTags } from "src/utils/request.js";
import avertStore from "src/avertStore";

export default {
  components: {
    ExportData,
  },
  setup() {
    let rows = ref([]);
    const filter = ref("");
    let selected = ref([]);

    fetchKeystrokes();
    rows.value = avertStore.state.keystrokes;
    return {
      selected,
      updateTags,
      filter,
      columns,
      rows,
    };
  },
};
</script>
