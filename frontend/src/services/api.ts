import axios from "axios";

const API = axios.create({
  baseURL: "/api", // don't hardcode 127.0.0.1
});

export const fetchTeam = async () => {
  const res = await API.get("/teams/");
  return res.data;
};
