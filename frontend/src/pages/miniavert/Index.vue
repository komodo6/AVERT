<template>
  <div class="">
    <div class="row items-center justify-center">
      <div class="col-6">
        <div>
          <q-list>
            <q-item>
              <q-item-section>
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
              </q-item-section>
            </q-item>
          </q-list>
        </div>
      </div>
    </div>
    <div class="row items-center justify-center q-ma-md">
      <div class="col-6">
        <div>
          <q-btn-group>
            <q-btn @click="startRecording"> Start </q-btn>
            <q-btn> Not Sure what goes here </q-btn>
            <q-btn @click="startRecording"> Stop </q-btn>
          </q-btn-group>
        </div>
      </div>
    </div>

    <div class="row items-center justify-center q-ma-md">
      <div class="col-6">
        <div>
          <q-btn @click="captureScreenshot"> capture screenshot </q-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";

import axios from "axios";
export default {
  data() {
    return {
      items: [
        { active: false, label: 'Record Keystrokes' }, 
        { active: false, label: 'Record Mouse' },
        { active: false, label: 'Record Screenshots' }, 
        { active: false, label: 'Record Processes' }, 
        { active: false, label: 'Record Window History' }, 
        { active: false, label: 'Record System Calls' },
        { active: false, label: 'Record Video' },
        { active: false, label: 'Record PCAP' },
      ],
      all: ref(false),
      options: ["Minutes", "Seconds"],
      text: ref(""),
    };
  },
  methods: {
    async toggleAll() {
      if (this.all) {
        this.items.forEach(element => {
          element.active = true;
        });
      } else {
        this.items.forEach(element => {
          element.active = false;
        });
      }
      this.toggle();
    },
    async toggle() {
      let post_data = {
        keystrokes: false, 
        mouse: false,
        screenshots: false, 
        processes: false, 
        window_history: false, 
        system_calls: false, 
        video: false, 
        pcap: false
      };
      let i = 0;
      for (var key in post_data) {
        if(!post_data.hasOwnProperty(key))
          continue;
        post_data[key] = this.items[i].active;
        i++;
      }

      console.log(post_data)

      const response = await axios.post(
        "http://localhost:5000/recording/",
        post_data
      );
      console.log(response);
    },
  },
  setup() {
    const startRecording = () => {
      console.log("recording starting");
    };
    const stopRecording = () => {
      console.log("recording stopping");
    };

    const captureScreenshot = async () => {
      axios.get("http://localhost:5000/screenshots/capture");
    };

    return {
      captureScreenshot,
      stopRecording,
      startRecording,
    };
  },
};
</script>

<style scoped>
.q-btn {
  background-color: dimgray;
}
</style>
