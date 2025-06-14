import { useEffect } from "react";
import { trackVisitor } from "@/services/api";

export const useTrackVisitor = () => {
  useEffect(() => {
    const privateIp = window.location.hostname;
    trackVisitor(privateIp);
  }, []);
};
