#!/usr/bin/ts-node
import * as ds from "./modules/DS";
//import { parse } from "./modules/parse";
let meeting: ds.Meeting = {title:"Programowanie", 
    date:new Date("2020-01-01 17:30"),
    duration:90}

console.log(meeting.date);

let actions: ds.Action[] = [ds.Action.DAY_EARLIER,
    ds.Action.DAY_LATER,
    ds.Action.HOUR_EARLIER];

ds.move(meeting, ds.Action.DAY_LATER);
ds.move(meeting, ds.Action.HOUR_LATER);

console.log(meeting.date);

//console.log(parse)

