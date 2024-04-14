import Navbar from "@/components/global/navbar";
import {ContainerScroll} from "@/components/global/container-scroll";
import {Button} from "@/components/ui/button";
import {HeroParallax} from "@/components/global/connect-parallax";
import {examples} from "@/lib/constants";
import Image from "next/image";
import Link from "next/link";
import React from "react";
import {Apple} from "lucide-react";

export default function Home() {
    return (
        <main className="flex items-center justify-center flex-col">
            <Navbar/>
            <section
                className="h-screen w-full  bg-neutral-950 rounded-md  !overflow-visible relative flex flex-col items-center  antialiased">
                <div className="absolute inset-0  h-full w-full items-center px-5 py-24 [background:radial-gradient(125%_125%_at_50%_10%,#000_35%,#223_100%)]"></div>
                <div className="flex flex-col mt-[-100px] md:mt-[-50px]">
                    <ContainerScroll titleComponent={
                        <div className="flex items-center flex-col">
                            <Button
                                size={'sm'}
                                className="p-8 mb-8 md:mb-0 text-2xl w-full sm:w-fit border-t-2 rounded-full border-[#4D4D4D] bg-[#F25C05] hover:bg-[#F29A2E] group transition-all flex items-center justify-center gap-4 hover:shadow-xl hover:shadow-neutral-500 duration-500"
                            >
                            <span
                                className="bg-clip-text text-white bg-gradient-to-r from-neutral-500 to-neutral-600  md:text-center font-sans  group-hover:from-white goup-hover:to-white group-hover:bg-gradient-to-r">
                                Get Started Now
                            </span>
                            </Button>
                            <h1 className="text-5xl md:text-8xl  bg-clip-text text-transparent bg-gradient-to-b from-white to-neutral-600 font-sans font-bold">
                                Waste Less, Feed More
                            </h1>
                        </div>
                    }/>
                </div>
            </section>

            {/* Empresas aportadoras */}

            <section>
                <HeroParallax examples={examples}></HeroParallax>
            </section>

            <section className="flex items-center justify-center flex-col">

            </section>

            <div className='mx-auto mb-32 mt-32 max-w-5xl sm:mt-56'>
                <div className='mb-12 px-6 lg:px-8'>
                    <div className='mx-auto max-w-2xl sm:text-center'>
                        <h2 className='mt-2 font-bold text-4xl text-white sm:text-5xl'>
                            Join the fight against food waste and hunger
                        </h2>
                        <p className='mt-4 text-lg text-gray-600'>
                            Connecting surplus food to fight hunger and waste.
                        </p>
                    </div>
                </div>

                {/* steps */}
                <ol className='my-8 space-y-4 pt-8 md:flex md:space-x-12 md:space-y-0'>
                    <li className='md:flex-1'>
                        <div
                            className='flex flex-col space-y-2 border-l-4 border-zinc-300 py-2 pl-4 md:border-l-0 md:border-t-2 md:pb-0 md:pl-0 md:pt-4'>
              <span className='text-sm font-medium text-primary'>
                Step 1
              </span>
                            <span className='text-xl font-semibold'>
                Sign up for an account
              </span>
                            <span className='mt-2 text-zinc-700'>
                If you already have an account, please{' '}
                                <Link
                                    href='/pricing'
                                    className='text-primary underline underline-offset-2'>
                  sign in.
                </Link>
                .
              </span>
                        </div>
                    </li>
                    <li className='md:flex-1'>
                        <div
                            className='flex flex-col space-y-2 border-l-4 border-zinc-300 py-2 pl-4 md:border-l-0 md:border-t-2 md:pb-0 md:pl-0 md:pt-4'>
              <span className='text-sm font-medium text-primary'>
                Step 2
              </span>
                            <span className='text-xl font-semibold'>
                Follow the intructions after
              </span>
                            <span className='mt-2 text-zinc-700'>
                We&apos;ll help you through the path
              </span>
                        </div>
                    </li>
                    <li className='md:flex-1'>
                        <div
                            className='flex flex-col space-y-2 border-l-4 border-zinc-300 py-2 pl-4 md:border-l-0 md:border-t-2 md:pb-0 md:pl-0 md:pt-4'>
              <span className='text-sm font-medium text-primary'>
                Step 3
              </span>
                            <span className='text-xl font-semibold'>
                Start helping thw world
              </span>
                            <span className='mt-2 text-zinc-700'>
                It&apos;s that simple. Try out FoodFinder today
              </span>
                        </div>
                    </li>
                </ol>

                <div className='mx-auto max-w-6xl px-6 lg:px-8'>
                    <div className='mt-16 flow-root sm:mt-24'>
                        <div
                            className='-m-0 rounded-xl bg-gray-900/5 p-0  lg:-m-4 lg:rounded-2xl lg:p4'>
                            <video
                                width={1472}
                                height={756}
                                controls preload="none"
                                className='rounded-md bg-white p-0 sm:p-8 md:p-5 shadow-2xl'
                                autoPlay
                            >
                            <source src="/videos/video.mp4" type="video/mp4"/>
                                Your browser does not support the videos.
                            </video>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    );
}
