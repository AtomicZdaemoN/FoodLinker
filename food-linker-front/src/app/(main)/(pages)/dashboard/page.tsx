import * as React from "react";
import Sidebar from "@/components/dashboard-components/sidebar";
import TopBar from "@/components/dashboard-components/top-bar";
import MainContent from "@/components/dashboard-components/main-component";
function Dashboard() {
    return (
        <div className="flex min-h-screen w-full flex-col bg-muted/40">
            <Sidebar />
            <div className="flex flex-col sm:gap-4 sm:py-4 sm:pl-14">
                <TopBar />
                <MainContent />
            </div>
        </div>
    );
}

export default Dashboard;
