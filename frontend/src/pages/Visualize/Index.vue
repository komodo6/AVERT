<template>
  <div class="viz-container">
    <div class="row">
      <div class="col-12">
        <div class="text-h3">Visualization</div>
        <div class="col-12">
          <div>
            <q-form>
              <div class="row">
                <div class="col-5">
                  <div class="row">
                    <div class="col">
                      <div class="text-subtitle1">Select Graph Type</div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-2.5">
                      <q-radio> Timeline </q-radio>
                    </div>
                    <div class="col-2.5">
                      <q-radio> Bar Graph </q-radio>
                    </div>
                    <div class="col-2.5">
                      <q-radio> Pie Chart </q-radio>
                    </div>
                    <div class="col-2.5">
                      <q-radio> CPU Usage </q-radio>
                    </div>
                  </div>
                </div>
                <div class="col-7">
                  <div class="row">
                    <div class="col">
                      <div class="text-subtitle1">Enter Time Frame</div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-4">
                      <div clas="start-date">
                        <label> Start Date</label>
                        <input type="datetime-local" />
                      </div>
                    </div>
                    <div class="col-4">
                      <div clas="end-date">
                        <label> End Date</label>
                        <input type="datetime-local" />
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-5">
                  <div class="row">
                    <div class="col-3">
                      <q-checkbox> Select All </q-checkbox>
                      <q-checkbox> Mouse Movements </q-checkbox>
                      <q-checkbox> PCAP </q-checkbox>
                    </div>
                    <div class="col-3">
                      <q-checkbox> Screenshots </q-checkbox>
                      <q-checkbox> Window Histories </q-checkbox>
                      <q-checkbox> Keystrokes </q-checkbox>
                    </div>
                  </div>
                </div>
                <div class="col-6">
                  <div class="row">
                    <div class="col">
                      <div class="text-subtitle1">Select Graph Interval</div>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-2">
                      <q-radio> Days</q-radio>
                    </div>
                    <div class="col-2">
                      <q-radio> Hours</q-radio>
                    </div>
                    <div class="col-2">
                      <q-radio> Minutes</q-radio>
                    </div>
                    <div class="col-2">
                      <q-radio> Seconds</q-radio>
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-5">
                      <q-btn @click="generateGraph" size="lg" color="grey-9">
                        Generate Graph
                      </q-btn>
                    </div>
                  </div>
                </div>
              </div>
            </q-form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref } from "vue";

export default {
  setup() {
    let sa = ref(false);
    let sc = ref(false);
    let mm = ref(false);
    let wh = ref(false);
    let pc = ref(false);
    let ks = ref(false);
    return {
      sa,
      sc,
      mm,
      wh,
      pc,
      ks,
      val: ref(true),
      int: ref(true),
    };
  },
};
</script>

<style scoped>
.viz-container {
  margin: 2em;
}
</style>
