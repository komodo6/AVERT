<template>
  <div>
    <div class="text-h2">SETTINGS</div>
    <div class="row">
      <div class="col">
        <div class="row">
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>Toggle All</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="all"
                    v-on:click="toggleAll()"
                  />
                </q-item-section>
              </q-item>
              <q-item v-for="item in items" :key="item.label">
                <q-item-section>
                  <q-item-label>{{ item.label }}</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="item.active"
                    v-on:click="toggle()"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>PCAP Creation Interval</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Idle Recording Threshold</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Process Capture Interval</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="row">
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>Frame Rate</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Resolution</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Video Length</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-input color="primary" v-model="text" />
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
          <div class="col">
            <q-list bordered>
              <q-item>
                <q-item-section>
                  <q-item-label>File Type</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-select
                    v-model="model"
                    :options="options"
                    label="Interval"
                  />
                </q-item-section>
              </q-item>
            </q-list>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <apexcharts
        width="550"
        type="pie"
        :options="chartOptions"
        :series="[
          avertStore.state.keystrokesCount,
          avertStore.state.systemcallsCount,
          avertStore.state.processesCount,
          avertStore.state.mouseactionsCount / 10,
          0,
          avertStore.state.screenshotsCount,
          avertStore.state.windowhistoryCount,
          avertStore.state.videosCount,
          1000,
        ]"
      ></apexcharts>
    </div>
  </div>
</template>
<script>
import { onMounted, ref } from "vue";
import { api } from "src/boot/axios";
import VueApexCharts from "vue3-apexcharts";
import {
  fetchKeystrokesCount,
  fetchMouseActionsCount,
  fetchScreenshotsCount,
  fetchProcessesCount,
  fetchWindowHistoryCount,
  fetchSystemCallsCount,
  fetchVideosCount,
} from "src/utils/request.js";
import avertStore from "src/avertStore";

export default {
  name: "Chart",
  components: {
    apexcharts: VueApexCharts,
  },
  setup() {
    let chartOptions = {
      chart: {
        width: 550,
        type: "pie",
      },
      labels: [
        "Keystrokes",
        "System Calls",
        "Processes",
        "Mouse Actions",
        "Network Data",
        "Screenshots",
        "Window History",
        "Video",
        "Remaining Storage",
      ],
      responsive: [
        {
          breakpoint: 480,
          options: {
            chart: {
              width: 200,
            },
            legend: {
              position: "bottom",
            },
          },
        },
      ],
      dataLabels: {
        style: {
          colors: [],
        },
      },
    };

    let items = ref([
      { active: false, label: "Record Keystrokes" },
      { active: false, label: "Record Mouse" },
      { active: false, label: "Record Screenshots" },
      { active: false, label: "Record Processes" },
      { active: false, label: "Record Window History" },
      { active: false, label: "Record System Calls" },
      { active: false, label: "Record Video" },
      { active: false, label: "Record PCAP" },
    ]);
    let all = ref(false);
    let options = ref(["Minutes", "Seconds"]);
    let text = ref("");

    onMounted(() => {
      fetchKeystrokesCount();
      fetchMouseActionsCount();
      fetchScreenshotsCount();
      fetchProcessesCount();
      fetchWindowHistoryCount();
      fetchSystemCallsCount();
      fetchVideosCount();
      console.log("onMounted");
    });

    const toggleAll = async () => {
      if (this.all) {
        items.value.forEach((element) => {
          element.active = true;
        });
      } else {
        items.value.forEach((element) => {
          element.active = false;
        });
      }
      toggle();
    };

    const toggle = async () => {
      let post_data = {
        keystrokes: false,
        mouse: false,
        screenshots: false,
        processes: false,
        window_history: false,
        system_calls: false,
        video: false,
        pcap: false,
      };
      let i = 0;
      for (var key in post_data) {
        if (!post_data.hasOwnProperty(key)) continue;
        post_data[key] = items.value[i].active;
        i++;
      }

      if (post_data.video) {
        await api.get("/videos/capture");
      } else if (!post_data.video) {
        await api.get("/videos/stop");
      }
      if (post_data.pcap) {
        await api.get("/networkdata/start");
      } else if (!post_data.pcap) {
        await api.get("/networkdata/stop");
      }

      console.log(post_data);

      const { response } = await api.post("/recording/", post_data);
      console.log(response);
    };

    return {
      toggleAll,
      toggle,
      items,
      all,
      options,
      text,
      chartOptions,
      avertStore,
    };
  },
};
</script>
<style lang=""></style>
