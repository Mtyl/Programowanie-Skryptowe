"use strict";
exports.__esModule = true;
exports.Timetable = exports.move = exports.Action = void 0;
var Action;
(function (Action) {
    Action[Action["DAY_EARLIER"] = 0] = "DAY_EARLIER";
    Action[Action["DAY_LATER"] = 1] = "DAY_LATER";
    Action[Action["HOUR_EARLIER"] = 2] = "HOUR_EARLIER";
    Action[Action["HOUR_LATER"] = 3] = "HOUR_LATER";
})(Action = exports.Action || (exports.Action = {}));
var move = function (meeting, action, timet) {
    var time = meeting.date.getTime();
    var hour = time % (3600 * 24 * 1000);
    var newTime;
    switch (action) {
        case Action.DAY_EARLIER:
            newTime = (time - 24 * 3600 * 1000);
            break;
        case Action.DAY_LATER:
            newTime = (time + 24 * 3600 * 1000);
            break;
        case Action.HOUR_EARLIER:
            if (hour - 3600000 < 3600 * 7000)
                return false;
            newTime = (time - 3600000);
            break;
        case Action.HOUR_LATER:
            if (hour + 3600000 + meeting.duration * 60000 > 3600 * 19000)
                return false;
            newTime = (time + 3600000);
            break;
    }
    if (timet) {
        var date = new Date(newTime);
        if (!timet.canBeTransferredTo(date, meeting.duration))
            return false;
    }
    meeting.date.setTime(newTime);
    return true;
};
exports.move = move;
var Timetable = /** @class */ (function () {
    function Timetable() {
        var _this = this;
        this.canBeTransferredTo = function (date, duration) {
            var intDate = date.getTime() % (24 * 3600 * 1000);
            if (!duration) {
                duration = 3600000;
            }
            else {
                duration *= 60000;
            }
            if (intDate >= 7000 * 3600
                && intDate + duration <= 19000 * 3600
                && !_this.busy(date, duration / 60000)) {
                return true;
            }
            return false;
        };
        this.busy = function (date, duration) {
            var intDate = date.getTime();
            if (!duration) {
                duration = 3600000;
            }
            else {
                duration *= 60000;
            }
            for (var _i = 0, _a = _this.meetingList; _i < _a.length; _i++) {
                var meeting = _a[_i];
                var busyDate = meeting.date.getTime();
                if (intDate >= busyDate &&
                    intDate <= busyDate + meeting.duration)
                    return true;
            }
            return false;
        };
        this.put = function (meeting) {
            if (_this.canBeTransferredTo(meeting.date, meeting.duration)) {
                _this.meetingList.push(meeting);
                return true;
            }
            return false;
        };
        this.get = function (date) {
            var intDate = date.getTime();
            for (var _i = 0, _a = _this.meetingList; _i < _a.length; _i++) {
                var meeting = _a[_i];
                if (intDate == meeting.date.getTime())
                    return meeting;
            }
            var noMeeting = { title: "ERROR",
                date: new Date(0), duration: 0 };
            return noMeeting;
        };
        this.perform = function (actions) {
            for (var i = 0; i < actions.length; i++) {
                exports.move(_this.meetingList[i % _this.meetingList.length], actions[i], _this);
            }
        };
        this.str = function (meeting) {
            var startHours = meeting.date.getHours();
            var startMinutes = meeting.date.getMinutes();
            var endingMinute = startMinutes + meeting.duration;
            var endingHours = startHours + Math.floor(endingMinute / 60);
            endingMinute %= 60;
            return meeting.title + " " + startHours + ":" + startMinutes + "-" + endingHours + ":" + endingMinute;
        };
        this.meetingList = [];
    }
    return Timetable;
}());
exports.Timetable = Timetable;
