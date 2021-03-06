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
        path: "/packetcapture/packetfileview",
        component: () => import("pages/PacketCapture/PacketFileView.vue"),
        name: "PacketCaptureFileView",
        props: true,
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
      {
        path: "/sync",
        component: () => import("pages/Sync/Index.vue"),
      },
      {
        path: "/delete",
        component: () => import("pages/Delete/Index.vue"),
      },
      {
        path: "/Annotation",
        component: () => import("pages/Annotation/Index.vue"),
      },
      {
        path: "/processes",
        component: () => import("pages/Processes/Index.vue"),
      },
      {
        path: "/systemcalls",
        component: () => import("pages/SystemCalls/Index.vue"),
      },
      {
        path: "/scripts",
        component: () => import("pages/Scripts/Index.vue")
      },
      {
        path: "/windows",
        component: () => import("pages/WindowHistory/Index.vue"),
      },
    ],
  },
  {
    path: "/miniavert",
    component: () => import("layouts/MiniAvertLayout.vue"),
    children: [
      {
        path: "",
        component: () => import("pages/miniavert/Index.vue"),
      },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "/:catchAll(.)",
    component: () => import("pages/Error404.vue"),
  },
];

export default routes;
