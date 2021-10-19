<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-bar class="q-electron-drag bg-black">
        <div>AVERT MINI</div>

        <q-space />

        <q-btn dense flat icon="minimize" @click="minimize" />
        <q-btn dense flat icon="crop_square" @click="toggleMaximize" />
        <q-btn dense flat icon="close" @click="closeApp" />
      </q-bar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { useStore } from "vuex";
import { defineComponent, ref, computed } from "vue";

export default defineComponent({
  name: "MainLayout",

  components: {},

  setup() {
    let store = useStore();

    let miniavert = computed(() => store.state.miniavert.miniavert_window);
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
        console.log(miniavert);
        miniavert.value.close();
      }
    }
    return {
      minimize,
      toggleMaximize,
      closeApp,
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
