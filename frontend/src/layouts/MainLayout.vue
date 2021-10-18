<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
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
                <q-btn color="grey-9 q-mx-sm">
          <router-link to="/visualize"> Visualize </router-link>
        </q-btn>
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
    title: "Quasar Awesome",
    caption: "Community Quasar projects",
    icon: "favorite",
    link: "https://awesome.quasar.dev",
  },
];

import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "MainLayout",

  components: {
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    const moveTo = () => {
      console.log(router);
      router.push({
        name: "keystrokes",
      });
    };

    return {
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
a {
  text-decoration: none;
  color: white;
}

.router-link-exact-active {
  color: orange;
}
</style>
