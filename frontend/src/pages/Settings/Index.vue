<template>
  <div>
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
                    v-on:click="toggleAll"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Record Screen</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="active[0]"
                    v-on:click="toggle('screen', 0)"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Record Keystrokes</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="active[1]"
                    v-on:click="toggle('keystrokes', 1)"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Record Screenshots</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="active[2]"
                    v-on:click="toggle('screenshots', 2)"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Record PCAP</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="active[3]"
                    v-on:click="toggle('pcap', 3)"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Record Window History</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="active[4]"
                    v-on:click="toggle('window', 4)"
                  />
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Record Cursor</q-item-label>
                </q-item-section>
                <q-item-section>
                  <q-toggle
                    color="primary"
                    v-model="active[5]"
                    v-on:click="toggle('cursor', 5)"
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
      <div class="col">.col</div>
    </div>
    <div class="row">
      <div class="col">.col</div>
    </div>
  </div>
</template>
<script>
import { ref } from "vue";
import axios from "axios";
export default {
  data() {
    return {
      active: [false, false, false, false, false, false],
      all: ref(false),
      options: ["Minutes", "Seconds"],
      text: ref(""),
    };
  },
  methods: {
    async toggleAll() {
      if (this.all) {
        for (let i in this.active) {
          this.active[i] = true;
        }
      } else {
        for (let i in this.active) {
          this.active[i] = false;
        }
      }
    },
    async toggle(recordType, i) {
      let data = { record: this.active[i], type: recordType };
      const response = await axios.post(
        "http://localhost:5000/recording/",
        data
      );
      console.log(response);
    },
  },
};
</script>
<style lang=""></style>
