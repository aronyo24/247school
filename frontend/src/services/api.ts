import axios from "axios";

const API = axios.create({
  baseURL: "/api", // don't hardcode 127.0.0.1
});

export const fetchTeam = async () => {
  const res = await API.get("/teams/");
  return res.data;
};
export const trackVisitor = async (privateIp: string) => {
  try {
    await API.post("/track-visitor/", {
      private_ip: privateIp,
    });
  } catch (error) {
    console.error("Visitor tracking failed:", error);
  }
};
