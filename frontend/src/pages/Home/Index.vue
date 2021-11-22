<template>
  <div class="q-pa-sm">
    <div class="row">
      <div class="col">
        <q-table
          title="All Artifacts"
          :rows="rows"
          :columns="columns"
          dark
          color="amber"
          selection="multiple"
          v-model:selected="selected"
          :filter="filter"
          row-key="id"
        >
          <template v-slot:top>
            <q-input
              dark
              dense
              standout
              v-model="filter"
              input-class="text-right"
              class="q-ml-md"
              label="Search"
            >
              <template v-slot:append>
                <q-icon v-if="filter === ''" name="search" />
                <q-icon
                  v-else
                  name="clear"
                  class="cursor-pointer"
                  @click="filter = ''"
                />
              </template>
            </q-input>

            <div class="row">
              <div class="datetime-from col-12">
                <input type="datetime-local" name="" id="" />
              </div>
              <div class="datetime-to col-12">
                <input type="datetime-local" name="" id="" />
              </div>
            </div>
          </template>

          <template v-slot:header="props">
            <q-tr :props="props">
              <q-th auto-width>
                <q-checkbox v-model="props.selected" />
              </q-th>
              <q-th auto-width />

              <q-th v-for="col in props.cols" :key="col.name" :props="props">
                {{ col.label }}
              </q-th>
            </q-tr>
          </template>

          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td>
                <q-checkbox v-model="props.selected" />
              </q-td>
              <q-td auto-width>
                <q-btn
                  size="sm"
                  color="accent"
                  round
                  dense
                  @click="props.expand = !props.expand"
                  :icon="props.expand ? 'remove' : 'add'"
                />
              </q-td>
              <q-td key="artifact" :props="props">
                {{ props.row.artifact }}
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
                <div v-for="annotation in props.row.annotations" :key="annotation">
                  {{annotation}}
                </div>
              </q-td>
              <q-td key="tags" :props="props">
                <q-select
                  class="align-right"
                  label="Tags"
                  filled
                  :v="props.row.tags"
                  v-model="props.row.tags"
                  @update:model-value="updateTags(props.row.tags, props.row.id, props.row.artifact)"
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
            <q-tr v-show="props.expand" :props="props">
              <q-td colspan="100%">
                <div class="row">
                  <div
                    class="col-5"
                    v-for="(value, key) in props.row"
                    :key="key"
                  >
                    {{ key }} : {{ value }}
                  </div>
                </div>
              </q-td>
            </q-tr>
          </template>
        </q-table>
        <q-input
          class="annotation"
          color="amber"
          outlined
          v-model="annotation"
          label="Your Annotation"
          :dense="dense"
        />

        <q-btn
          class="annotateBtn"
          color="grey-9 q-mx-sm"
          @click="saveAnnotation()"
          label="Add Annotation"
        />
      </div>
    </div>
  </div>
</template>

<script>
// const { desktopCapturer } = require("electron");
import { defineComponent, ref, computed, onMounted } from "vue";

const columns = [
  {
    name: "artifact",
    label: "Artifact",
    field: "artifact",
    align: "center",
    sortable: true,
  },
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

import axios from "axios";

import { exportFile, useQuasar } from "quasar";

export default {
  setup() {
    let rows = ref([]);
    let selected = ref([]);
    let filter = ref("");
    let annotation = ref("");
    let visibleColumns = ref([
      "calories",
      "desc",
      "fat",
      "carbs",
      "protein",
      "sodium",
      "calcium",
      "iron",
    ]);

    const saveAnnotation = () => {
      console.log(selected.value);
      for (const s of selected.value) {
        s.annotations = s.annotations.concat(annotation.value);
        updateAnnotations(s.annotations, s.id, s.artifact);
      }
      annotation.value = "";
    };

    const updateAnnotations = async (val, id, artifact) => {
      if (!val) {
        val = [];
      }
      await axios.post(`http://localhost:5000/${artifact}/annotations`, {
        id: id,
        annotation: val,
      });
      console.log(val, id);
    };

    const updateTags = async (val, id, artifact) => {
      if (!val) {
        val = [];
      }
      await axios.post(`http://localhost:5000/${artifact}/tags`, {
        id: id,
        tags: val,
      });
      console.log(val, id);
    };

    const fetchKeystrokes = async () => {
      const { data } = await axios.get("http://192.168.19.132:5000/keystrokes");
      for (const d of data) {
        d["artifact"] = "keystroke";
      }
      rows.value = data;
    };
    const fetchSystemCalls = async () => {
      const { data } = await axios.get(
        "http://192.168.19.132:5000/systemcalls"
      );
      for (const d of data) {
        d["artifact"] = "systemcall";
      }
      rows.value = rows.value.concat(data);
    };
    const fetchProcesses = async () => {
      const { data } = await axios.get("http://192.168.19.132:5000/processes");
      for (const d of data) {
        d["artifact"] = "process";
      }
      rows.value = rows.value.concat(data);
    };
    const fetchMouseactions = async () => {
      const { data } = await axios.get(
        "http://192.168.19.132:5000/mouseactions"
      );
      for (const d of data) {
        d["artifact"] = "mouseaction";
      }
      rows.value = rows.value.concat(data);
    };
    const fetchImages = async () => {
      let { data } = await axios.get(
        "http://192.168.19.132:5000/screenshots/images"
      );
      for (const d of data) {
        d["artifact"] = "screenshot";
      }
      rows.value = rows.value.concat(data);
    };
    const fetchWindows = async () => {
      let { data } = await axios.get("http://192.168.19.132:5000/windows");
      for (const d of data) {
        d["artifact"] = "window";
      }
      rows.value = rows.value.concat(data);
    };
    const fetchVideos = async () => {
      let { data } = await axios.get(
        "http://192.168.19.132:5000/videos/videos"
      );
      for (const d of data) {
        d["artifact"] = "video";
      }
      rows.value = rows.value.concat(data);
    };

    onMounted(() => {
      fetchKeystrokes();
      fetchMouseactions();
      fetchSystemCalls();
      fetchProcesses();
      fetchImages();
      fetchWindows();
      fetchVideos();
    });

    const plusOne = computed(() => visibleColumns);
    console.log(plusOne);
    return {
      selected,
      visibleColumns,
      rows,
      columns,
      filter,
      updateTags,
      saveAnnotation,
      annotation,
    };
  },
};
</script>
