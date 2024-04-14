'use client'

import React from "react";
import {
    motion,
    useScroll,
    useTransform,
    useSpring,
    MotionValue,
} from 'framer-motion'
import Image from 'next/image'
import Link from 'next/link'

export const HeroParallax = ({
    examples,
}: {
    examples: {
        thumbnail: string
    }[]
}) => {
    const firstRow = examples.slice(0, 5)
    const secondRow = examples.slice(5, 10)
    const thirdRow = examples.slice(10, 15)
    const ref = React.useRef(null)
    const { scrollYProgress } = useScroll({
        target: ref,
        offset: ['start start', 'end start'],
    })

    const springConfig = { stiffness: 300, damping: 30, bounce: 100 }

    const translateX = useSpring(
        useTransform(scrollYProgress, [0, 1], [0, 1000]),
        springConfig
    )
    const translateXReverse = useSpring(
        useTransform(scrollYProgress, [0, 1], [0, -1000]),
        springConfig
    )
    const rotateX = useSpring(
        useTransform(scrollYProgress, [0, 0.2], [15, 0]),
        springConfig
    )
    const opacity = useSpring(
        useTransform(scrollYProgress, [0, 1.2], [0.1, 1]),
        springConfig
    )
    const rotateZ = useSpring(
        useTransform(scrollYProgress, [0, 0.2], [20, 0]),
        springConfig
    )
    const translateY = useSpring(
        useTransform(scrollYProgress, [0, 0.5], [-700, 0]),
        springConfig
    )
    return (
        <div
            ref={ref}
            className="h-[250vh] py-40 overflow-hidden  antialiased relative flex flex-col self-auto [perspective:800px] [transform-style:preserve-3d]"
        >
            <Header />
            <motion.div
                style={{
                    rotateX,
                    rotateZ,
                    translateY,
                    opacity,
                }}
                className=""
            >
                <motion.div className="flex flex-row-reverse space-x-reverse space-x-20 mb-20">
                    {firstRow.map((example) => (
                        <ExampleCard
                            example={example}
                            translate={translateX}
                        />
                    ))}
                </motion.div>
                <motion.div className="flex flex-row  mb-20 space-x-20 ">
                    {secondRow.map((example) => (
                        <ExampleCard
                            example={example}
                            translate={translateXReverse}
                        />
                    ))}
                </motion.div>
                <motion.div className="flex flex-row-reverse space-x-reverse space-x-20">
                    {thirdRow.map((example) => (
                        <ExampleCard
                            example={example}
                            translate={translateX}
                        />
                    ))}
                </motion.div>
            </motion.div>
        </div>
    )
}

export const Header = () => {
    return (
        <div className="max-w-7xl relative mx-auto py-40 md:py-40 px-4 w-full right-0 top-0">
            <h1 className="text-2xl md:text-7xl font-bold dark:text-white">
                 Every scrap saved <br /> is a meal earned
            </h1>
            <p className="max-w-2xl text-base md:text-xl mt-8 dark:text-white">
                We are passionate about making a positive impact on both the environment and communities in need. We are dedicated to addressing the pressing issues of food waste and scarcity by creating a bridge between surplus food and those who need it most. Through our innovative platform, we connect surplus food sources with organizations and individuals who can utilize it effectively, reducing waste and combating hunger simultaneously. Our mission is not only to alleviate food insecurity but also to promote sustainability and responsible consumption practices. By harnessing the power of technology and collaboration, we strive to create a world where every meal matters and where no one goes hungry
            </p>
        </div>
    )
}

export const ExampleCard = ({
    example,
    translate,
}: {
    example: {
        thumbnail: string
    }
    translate: MotionValue<number>
}) => {
    return (
        <motion.div
            style={{
                x: translate,
            }}
            className="group/example h-80 w-[35rem] relative flex-shrink-0"
        >
                <Image
                    src={example.thumbnail}
                    height="400"
                    width="400"
                    className="object-cover object-left-top absolute h-full w-full inset-0"
                    alt=""
                />
            <div className="absolute inset-0 h-full w-full opacity-0 bg-black pointer-events-none"></div>

        </motion.div>
    )
}