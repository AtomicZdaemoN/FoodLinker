import * as React from "react";
import Sidebar from "@/components/dashboard-components/sidebar";
import TopBar from "@/components/dashboard-components/top-bar";
import EditProductComponent from "@/components/dashboard-components/edit-product-component";
function EditProduct() {
    return (
        <div className="flex min-h-screen w-full flex-col bg-muted/40">
            <Sidebar />
            <div className="flex flex-col sm:gap-4 sm:py-4 sm:pl-14">
                <TopBar />
                <EditProductComponent />
            </div>
        </div>
    );
}

export default EditProduct;
