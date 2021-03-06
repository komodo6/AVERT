import { store } from "quasar/wrappers";
import { createStore } from "vuex";

// import example from './module-example'

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

const screenshots = {
  namespace: true,
  state: {
    screenshots: [],
  },
};

const Videos = {
  namespace: true,
  state: {
    Videos: [],
  },
};

const miniavert = {
  namespace: true,
  state: {
    miniavert_window: null,
  },
};

export default store(function (/* { ssrContext } */) {
  const Store = createStore({
    modules: {
      screenshots,
      miniavert,
      Videos
      // example
    },

    // enable strict mode (adds overhead!)
    // for dev mode and --debug builds only
    // strict: process.env.DEBUGGING
  });

  return Store;
});
