const routes = [
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [
      { path: "", component: () => import("pages/Home/Index.vue") },
      {
        path: "/keystrokes",
        component: () => import("pages/Keystrokes/Index.vue"),
      },
      {
        path: "/mouseactions",
        component: () => import("pages/MouseActions/Index.vue"),
      },
      {
        path: "/packetcapture",
        component: () => import("pages/PacketCapture/Index.vue"),
      },
      {
        path: "/screenshots",
        component: () => import("pages/Screenshots/Index.vue"),
      },
      {
        path: "/settings",
        component: () => import("pages/Settings/Index.vue"),
      },
      {
        path: "/transactions",
        component: () => import("pages/Transactions/Index.vue"),
      },
      { path: "/videos", component: () => import("pages/Videos/Index.vue") },
      {
        path: "/visualize",
        component: () => import("pages/Visualize/Index.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.*)*",
    component: () => import("pages/Error404.vue"),
  },
];

export default routes;
