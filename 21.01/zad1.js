#!/usr/bin/ts-node
"use strict";
exports.__esModule = true;
var ds = require("./modules/DS");
var meeting = { title: "Programowanie",
    date: new Date("2020-01-01 17:30"),
    duration: 90 };
console.log(meeting.date);
var actions = [ds.Action.DAY_EARLIER,
    ds.Action.DAY_LATER,
    ds.Action.HOUR_EARLIER];
ds.move(meeting, ds.Action.DAY_LATER);
ds.move(meeting, ds.Action.HOUR_LATER);
console.log(meeting.date);
