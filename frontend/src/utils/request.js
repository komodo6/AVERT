import { api } from "src/boot/axios";
import avertStore from "src/avertStore";

export const fetchKeystrokes = async () => {
  await api.get("/keystrokes").then((response) => {
    response.data["artifact"] = "keystroke";
    avertStore.state.keystrokes = response.data;
  });
};

export const fetchMouseActions = async () => {
  await api.get("/mouseactions").then((response) => {
    response.data["artifact"] = "mouseaction";
    avertStore.state.mouseactions = response.data;
  });
};

export const fetchMouseActionsTimeline = async () => {
  await api.post("/mouseactions/timeline", {
    start: "start",
    end: "end",
  });
};

export const fetchScreenshots = async () => {
  await api.get("/screenshots").then((response) => {
    response.data["artifact"] = "screenshot";
    avertStore.state.screenshots = response.data;
  });
};

export const fetchProcesses = async () => {
  await api.get("/processes").then((response) => {
    response.data["artifact"] = "processe";
    avertStore.state.processes = response.data;
  });
};

export const fetchWindowHistory = async () => {
  await api.get("/windows").then((response) => {
    response.data["artifact"] = "window";
    avertStore.state.windowhistory = response.data;
  });
};

export const fetchSystemCalls = async () => {
  await api.get("/systemcalls").then((response) => {
    response.data["artifact"] = "systemcall";
    avertStore.state.systemcalls = response.data;
  });
};

export const fetchVideos = async () => {
  await api.get("/videos").then((response) => {
    response.data["artifact"] = "video";
    avertStore.state.videos = response.data;
  });
};

export const fetchKeystrokesCount = async () => {
  await api.get("/keystrokes/count").then((response) => {
    avertStore.state.keystrokesCount = response.data;
  });
};

export const fetchMouseActionsCount = async () => {
  await api.get("/mouseactions/count").then((response) => {
    console.log(response.data);
    avertStore.state.mouseactionsCount = response.data;
  });
};

export const fetchScreenshotsCount = async () => {
  await api.get("/screenshots/count").then((response) => {
    console.log(response.data);
    avertStore.state.screenshotsCount = response.data;
  });
};

export const fetchProcessesCount = async () => {
  await api.get("/processes/count").then((response) => {
    console.log(response.data);
    avertStore.state.processesCount = response.data;
  });
};

export const fetchWindowHistoryCount = async () => {
  await api.get("/windows/count").then((response) => {
    console.log(response.data);
    avertStore.state.windowhistoryCount = response.data;
  });
};

export const fetchSystemCallsCount = async () => {
  await api.get("/systemcalls/count").then((response) => {
    console.log(response.data);
    avertStore.state.systemcallsCount = response.data;
  });
};

export const fetchVideosCount = async () => {
  await api.get("/videos/count").then((response) => {
    console.log(response.data);
    avertStore.state.videosCount = response.data;
  });
};

export const updateAnnotations = async (val, id, artifact) => {
  await api.post(`/${artifact}s/annotations`, {
    id: id,
    annotation: val,
  });
  console.log(val, id);
};

export const updateTags = async (val, id, artifact) => {
  if (!val) {
    val = [];
  }
  await api.post(`/${artifact}s/tags`, {
    id: id,
    tags: val,
  });
  console.log(val, id);
};