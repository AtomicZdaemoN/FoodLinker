import Link from "next/link";
import {ShoppingCart, Package, Settings, Apple, Archive} from "lucide-react";
import {Tooltip, TooltipContent, TooltipProvider, TooltipTrigger} from "@/components/ui/tooltip";

function Sidebar() {
    return (
        <aside className="fixed inset-y-0 left-0 z-10 hidden w-14 flex-col border-r bg-background sm:flex">
            <nav className="flex flex-col items-center gap-4 px-2 py-4">
                <TooltipProvider>
                    <Link
                        href="/dashboard"
                        className="group flex h-9 w-9 shrink-0 items-center justify-center gap-2 rounded-full bg-primary text-lg font-semibold text-primary-foreground md:h-8 md:w-8 md:text-base"
                    >
                        <Apple className="h-4 w-4 transition-all group-hover:scale-110 text-white"/>
                        <span className="sr-only">FoodLinker</span>
                    </Link>

                    <Tooltip>
                        <TooltipTrigger asChild>
                            <Link
                                href="/dashboard/orders"
                                className="flex h-9 w-9 items-center justify-center rounded-lg transition-colors hover:text-foreground md:h-8 md:w-8"
                            >
                                <ShoppingCart className="h-5 w-5"/>
                                <span className="sr-only">Orders</span>
                            </Link>
                        </TooltipTrigger>
                        <TooltipContent side="right">Orders</TooltipContent>
                    </Tooltip>
                    <Tooltip>
                        <TooltipTrigger asChild>
                            <Link
                                href="/dashboard/products"
                                className="flex h-9 w-9 items-center justify-center rounded-lg bg-accent text-accent-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                            >
                                <Package className="h-5 w-5"/>
                                <span className="sr-only">Products</span>
                            </Link>
                        </TooltipTrigger>
                        <TooltipContent side="right">Products</TooltipContent>
                    </Tooltip>
                    <Tooltip>
                        <TooltipTrigger asChild>
                            <Link
                                href="/dashboard/playground"
                                className="flex h-9 w-9 items-center justify-center rounded-lg bg-accent text-accent-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                            >
                                <Archive className="h-5 w-5"/>
                                <span className="sr-only">Playground</span>
                            </Link>
                        </TooltipTrigger>
                        <TooltipContent side="right">Playground</TooltipContent>
                    </Tooltip>

                </TooltipProvider>
            </nav>
            <nav className="mt-auto flex flex-col items-center gap-4 px-2 py-4">
                <TooltipProvider>
                    <Tooltip>
                        <TooltipTrigger asChild>
                            <Link
                                href="#"
                                className="flex h-9 w-9 items-center justify-center rounded-lg text-muted-foreground transition-colors hover:text-foreground md:h-8 md:w-8"
                            >
                                <Settings className="h-5 w-5"/>
                                <span className="sr-only">Settings</span>
                            </Link>
                        </TooltipTrigger>
                        <TooltipContent side="right">Settings</TooltipContent>
                    </Tooltip>
                </TooltipProvider>
            </nav>

        </aside>
    );
}

export default Sidebar;
