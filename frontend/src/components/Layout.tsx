import React from "react";
import Header from "./Header";
import { useTrackVisitor } from "@/hooks/useTrackVisitor";
import { Outlet } from "react-router-dom";

const Layout: React.FC = () => {
  useTrackVisitor();

  return (
    <div className="min-h-screen">
      <Header />
      <main>
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;