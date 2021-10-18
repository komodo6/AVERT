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

        <q-toolbar-title> AVERT </q-toolbar-title>

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
        <q-btn @click="test"> capture </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> Essential Links </q-item-label>

        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
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
    title: "Discord Chat Channel",
    caption: "chat.quasar.dev",
    icon: "chat",
    link: "https://chat.quasar.dev",
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
export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
  },

  setup() {
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
    };

    const leftDrawerOpen = ref(false);

    const moveTo = () => {
      console.log(router);
      router.push({
        name: "keystrokes",
      });
    };

    function test() {
      if (process.env.MODE === "electron") {
        window.screenCaptureAPI.screenCapture();
        // console.log(window.electron);
      }
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
