<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-bar class="q-electron-drag bg-black">
        <div>AVERT</div>

        <q-space />

        <q-btn dense flat icon="minimize" @click="minimize" />
        <q-btn dense flat icon="crop_square" @click="toggleMaximize" />
        <q-btn dense flat icon="close" @click="closeApp" />
      </q-bar>
      <q-toolbar class="bg-dark">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-btn color="grey-9 q-mx-sm">
          <router-link to="/"> Home </router-link>
        </q-btn>

        <q-btn color="grey-9 q-mx-sm">
          <router-link to="/keystrokes"> Keystroke </router-link>
        </q-btn>

        <q-btn color="grey-9 q-mx-sm">
          <router-link to="/mouseactions"> Mouse Actions </router-link>
        </q-btn>

        <q-btn color="grey-9 q-mx-sm">
          <router-link to="/packetcapture"> Packet Capture </router-link>
        </q-btn>

        <q-btn color="grey-9 q-mx-sm">
          <router-link to="/screenshots"> Screenshots </router-link>
        </q-btn>

        <q-btn color="grey-9 q-mx-sm">
          <router-link to="/videos"> Videos </router-link>
        </q-btn>
        
          <q-btn color="grey-9 q-mx-sm"> <router-link to="/processes">Processes</router-link></q-btn>
        <router-link to="/systemcalls">
          <q-btn color="grey-9 q-mx-sm"> System Calls</q-btn>
        </router-link>
        <router-link to="/windows">
          <q-btn color="grey-9 q-mx-sm"> Window History</q-btn>
        </router-link>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> MAIN MENU </q-item-label>

        <q-item :clickable="false">
          <q-item-section>
            <a>
              <q-btn
                @click="test"
                style="width: 200px"
                icon="close_fullscreen"
                label="miniAvert"
                color="grey-9 q-mx-sm"
                push
              >
              </q-btn
            ></a>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/sync">
              <q-btn
                style="width: 200px"
                icon="sync"
                label="sync"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/transaction">
              <q-btn
                style="width: 200px"
                icon="article"
                label="transaction"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/visualize">
              <q-btn
                style="width: 200px"
                icon="auto_graph"
                label="visualize"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/delete">
              <q-btn
                style="width: 200px"
                icon="delete"
                label="delete"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/Annotation">
              <q-btn
                style="width: 200px"
                icon="delete"
                label="Annotate"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/export">
              <q-btn
                style="width: 200px"
                icon="north_east"
                label="export"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/settings">
              <q-btn
                style="width: 200px"
                icon="settings"
                label="settings"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

        <q-item :clickable="false">
          <q-item-section>
            <router-link to="/scripts">
              <q-btn
                style="width: 200px"
                icon="history_edu"
                label="scripts"
                color="grey-9 q-mx-sm"
                push
              />
            </router-link>
          </q-item-section>
        </q-item>

      </q-list>
    </q-drawer>

    <q-footer elevated>
      <q-toolbar class="bg-dark">
        <q-toolbar-title></q-toolbar-title>
        <q-btn class="q-ma-md" @click="captureScreenshot" color="grey-9">
          Capture Screenshot
        </q-btn>
        <q-btn
          class="q-ma-md"
          :class="{ recording: recordState }"
          color="grey-9"
          @click="startRecording"
        >
          {{ recordText }}
        </q-btn>
      </q-toolbar>
    </q-footer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import router from "../router/routes";
import EssentialLink from "components/EssentialLink.vue";

const linksList = [
  {
    title: "Docs",
    caption: "quasar.dev",
    icon: "school",
    link: "https://quasar.dev",
  },
  {
    title: "Github",
    caption: "github.com/quasarframework",
    icon: "code",
    link: "https://github.com/quasarframework",
  },
  {
    title: "Avert",
    caption: "chat.quasar.dev",
    icon: "chat",
    link: "http://localhost:8080/#/miniavert",
  },
  {
    title: "Forum",
    caption: "forum.quasar.dev",
    icon: "record_voice_over",
    link: "https://forum.quasar.dev",
  },
  {
    title: "Twitter",
    caption: "@quasarframework",
    icon: "rss_feed",
    link: "https://twitter.quasar.dev",
  },
  {
    title: "Facebook",
    caption: "@QuasarFramework",
    icon: "public",
    link: "https://facebook.quasar.dev",
  },
  {
    title: "Settings",
    caption: "",
    icon: "settings",
    link: "https://awesome.quasar.dev",
  },
];

import { defineComponent, ref } from "vue";
import axios from "axios";
import { useStore } from "vuex";
export default defineComponent({
  name: "MainLayout",

  components: {},

  setup() {
    let store = useStore();
    let recordState = ref(false);
    let recordText = ref("Start Recording");

    const startRecording = () => {
      if (recordState.value) {
        recordState.value = false;
        recordText.value = "Start Recording";
      } else {
        recordState.value = true;
        recordText.value = "Stop Recording";
      }
    };

    const captureScreenshot = async () => {
      axios.get("http://localhost:5000/screenshots/capture");
      location.reload()
    };

    const leftDrawerOpen = ref(false);

    const moveTo = () => {
      console.log(router);
      router.push({
        name: "keystrokes",
      });
    };

    function test() {
      store.state.miniavert.miniavert_window = window.open(
        process.env.APP_URL + "/#/miniavert",
        "_black",
        "top=500,left=200,frame=true,nodeIntegration=yes,height=500,widht=300,maxHeight=500,maxWidth=400,alwaysOnTop,closable=true"
      );
    }

    function minimize() {
      if (process.env.MODE === "electron") {
        window.myWindowAPI.minimize();
      }
    }

    function toggleMaximize() {
      if (process.env.MODE === "electron") {
        window.myWindowAPI.toggleMaximize();
      }
    }

    function closeApp() {
      if (process.env.MODE === "electron") {
        window.myWindowAPI.close();
      }
    }

    return {
      captureScreenshot,
      recordState,
      recordText,
      startRecording,
      minimize,
      toggleMaximize,
      closeApp,
      test,
      essentialLinks: linksList,
      moveTo,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>

<style lang="scss">
.recording {
  background-color: red !important;
}
a {
  text-decoration: none;
  color: white;
}

.router-link-exact-active {
  color: orange;
}
</style>
