<template>
  <div>
    <q-table
      :columns="columns"
      :rows="screenshots"
      v-model="selectedScreenshots"
      row-key="name"
    >
      <template v-slot:body="props">
        <q-tr :props="props">
          <q-td key="timestamp" :props="props">
            {{ props.row.timestamp }}
          </q-td>
          <q-td key="ip_address" :props="props">
            {{ props.row.ip_address }}
          </q-td>
          <q-td key="mac_address" :props="props">
            {{ props.row.mac_address }}
          </q-td>
          <q-td key="ScreenshotSize" :props="props">
            {{ props.row.ScreenshotSize }}
          </q-td>
          <q-td key="ScreenshotFormat" :props="props">
            {{ props.row.ScreenshotFormat }}
          </q-td>
          <q-td key="annotations" :props="props">
            {{ props.row.annotations }}
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
    name: "ScreenshotSize",
    label: "Screenshot Size",
    field: "ScreenshotSize",
    align: "center",
    sortable: true,
  },
  {
    name: "ScreenshotFormat",
    label: "Screenshot Format",
    field: "ScreenshotFormat",
    align: "center",
    sortable: true,
  },
  {
    name: "annotations",
    label: "Annotations",
    field: "annotations",
    align: "center",
    sortable: true,
  },
  {
    name: "tags",
    label: "Tags",
    field: "tags",
    align: "center",
    sortable: true,
  },
];
import { ref, computed } from "vue";
import { useStore } from "vuex";
import axios from "axios";
export default {
  setup() {
    let store = useStore();

    let screenshots = computed(() => store.state.screenshots.screenshots);

    let selectedScreenshots = ref(null);

    const updateTags = async (val, id) => {
      if (!val) {
        val = [];
      }
      await axios.post("http://192.168.169.128:5000/screenshots/image", {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };
    return {
      updateTags,
      screenshots,
      columns,
      selectedScreenshots,
    };
  },
};
</script>
