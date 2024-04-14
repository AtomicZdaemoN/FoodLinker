import React from 'react'
import Link from 'next/link';
import { MenuIcon, Apple } from 'lucide-react'
import {Button} from "@/components/ui/button";


type Props = {}

const Navbar = async (props: Props) => {
    return (
        <header className='fixed right-0 left-0 top-0 py-4 px-4 bg-black/40 backdrop-blur-lg z-[100] flex items-center border-b-[1px] border-neutral-900 justify-between'>
            <aside className="flex items-center gap-[2px]">
                <p className="text-3xl font-bold">Fo</p>
                <Apple className="text-primary"/>
                <p className="text-3xl font-bold">dLinker</p>
            </aside>
            <nav className="absolute left-[50%] top-[50%] transform translate-x-[-50%] translate-y-[-50%] hidden md:block">
                <ul className="flex items-center gap-4 list-none">
                    <li>
                        <Link href="#">Home</Link>
                    </li>
                    <li>
                        <Link href="#">Canals</Link>
                    </li>

                    <li>
                        <Link href="#">Contact</Link>
                    </li>

                </ul>
            </nav>
            <aside className="flex items-center gap-4">
                <Button variant="ghost">
                    <Link href='/sign-in'>Log in</Link>
                </Button>
                <Link
                    href="/sign-up"
                    className="relative inline-flex h-10 overflow-hidden rounded-full p-[2px] focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2 focus:ring-offset-slate-50"
                >
                    <span className="absolute inset-[-1000%] animate-[spin_2s_linear_infinite] bg-[conic-gradient(from_90deg_at_50%_50%,#F29A2E_0%,#F25C05_50%,#F29A2E_100%)]" />
                    <span className="inline-flex h-full w-full cursor-pointer items-center justify-center rounded-full bg-slate-950 px-3 py-1 text-sm font-medium text-white backdrop-blur-3xl">
                        Get Started
                    </span>
                </Link>
                <MenuIcon className="md:hidden" />
            </aside>
        </header>
    )
}

export default Navbar