#!/usr/bin/ts-node
import * as ds from "./modules/DS";
//import { parse } from "./modules/parse.js";

let meetings: ds.Meeting[] = [{title:"Programowanie JAVA", 
        date:new Date("2020-01-01 16:00"),
        duration:90}, {title:"Spotkanie z AVG", 
        date:new Date("2020-01-01 19:00"),
        duration:60}, {title:"BHP", 
        date:new Date("2020-01-01 15:30"),
        duration:30}];

//let x = parse(["h+", "h-"]);
//console.log(x);