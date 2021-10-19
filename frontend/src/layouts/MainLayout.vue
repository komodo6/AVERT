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
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> MAIN MENU </q-item-label>
        
        <q-item
          clickable
          tag="a"
          target="_blank"
          href="http://localhost:8080/#/miniavert"
        >
          <q-item-section>
            <q-btn style = "width:200px;" icon="close_fullscreen" label="miniAvert" color="grey-9 q-mx-sm" push />
          </q-item-section>
        </q-item>

         <q-item>
          <q-item-section>
            
              <router-link to="/sync"> <q-btn style = "width:200px;" icon="sync" label="sync" color="grey-9 q-mx-sm" push/> </router-link> 
              
          </q-item-section>
        </q-item>

        <q-item>
          <q-item-section>
            <router-link to="/transaction"> <q-btn style = "width:200px;" icon="article" label="transaction" color="grey-9 q-mx-sm" push/> </router-link> 
          </q-item-section>
        </q-item>
        
        <q-item>
          <q-item-section>
            <router-link to="/visualize"> <q-btn style = "width:200px;" icon="auto_graph" label="visualize" color="grey-9 q-mx-sm" push/> </router-link> 
          </q-item-section>
        </q-item>

        <q-item>
          <q-item-section>
            <router-link to="/delete"> <q-btn style = "width:200px;" icon="delete" label="delete" color="grey-9 q-mx-sm" push/> </router-link> 
          </q-item-section>
        </q-item>

        <q-item>
          <q-item-section>
            <router-link to="/annotate"> <q-btn style = "width:200px;" icon="edit" label="annotate" color="grey-9 q-mx-sm" push/> </router-link> 
          </q-item-section>
        </q-item>

        <q-item>
          <q-item-section>
            <router-link to="/export"> <q-btn style = "width:200px;" icon="north_east" label="export" color="grey-9 q-mx-sm" push/> </router-link> 
          </q-item-section>
        </q-item>

        <q-item>
          <q-item-section>
            <router-link to="/settings"> <q-btn style = "width:200px;" icon="settings" label="settings" color="grey-9 q-mx-sm" push/> </router-link> 
          </q-item-section>
        </q-item>

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
    title: "Quasar Awesome",
    caption: "Community Quasar projects",
    icon: "favorite",
    link: "https://awesome.quasar.dev",
  },
];

import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "MainLayout",

  components: {},

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