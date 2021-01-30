

export enum Action{
    DAY_EARLIER,
    DAY_LATER,
    HOUR_EARLIER,
    HOUR_LATER
}

export interface Meeting{
    title:string;
    date:Date;
    duration:number;
    participants?:string;
}

export let move: (x:Meeting, y:Action, z?:Timetable) => boolean =
    (meeting:Meeting, action:Action, timet?:Timetable) => {
        let time = meeting.date.getTime();
        let hour = time % (3600 * 24 * 1000);
        let newTime;
        switch(action){
            case Action.DAY_EARLIER:
                newTime = (time - 24*3600*1000);
                break;
            case Action.DAY_LATER:
                newTime = (time + 24*3600*1000);
                break;
            case Action.HOUR_EARLIER:
                if(hour-3600000 < 3600 * 7000)
                    return false;
                newTime = (time - 3600000);
                break;
            case Action.HOUR_LATER:
                if(hour+3600000+meeting.duration*60000 > 3600 * 19000)
                    return false;
                newTime = (time + 3600000);
                break;
        }
        if(timet){
            let date = new Date(newTime);
            if(!timet.canBeTransferredTo(date, meeting.duration))
            return false;
        }
        meeting.date.setTime(newTime);
        return true;
    }

interface ITimetable{
    canBeTransferredTo(date: Date): boolean,
    busy(date: Date): boolean,
    put(meeting: Meeting): boolean,
    get(date: Date): Meeting,
    perform(actions: Array<Action>): void
}

export class Timetable implements ITimetable {
    private meetingList:Meeting[]
    constructor(){
        this.meetingList = [];
    }
    canBeTransferredTo = (date:Date, duration?: number) => {
        let intDate = date.getTime() % (24*3600*1000);
        if(!duration){
            duration = 3600000;
        }else{
            duration *= 60000;
        }
        if(intDate >= 7000 * 3600 
            && intDate + duration <= 19000 * 3600
            && !this.busy(date, duration/60000)){
        return true;}
        return false;

    }
    busy = (date: Date, duration?: number) => {
        let intDate = date.getTime();
        if(!duration){
            duration = 3600000;
        }else{
            duration *= 60000;
        }
        for(let meeting of this.meetingList){
            let busyDate = meeting.date.getTime();
            if(intDate >= busyDate && 
                intDate <= busyDate + meeting.duration)
            return true;
        }
        return false;
    }
    put = (meeting: Meeting) => {
        if(this.canBeTransferredTo(meeting.date, meeting.duration)){
            this.meetingList.push(meeting);
            return true;
        }
        return false;
    }
    get = (date: Date) => {
        let intDate = date.getTime();
        for(let meeting of this.meetingList){
            if(intDate == meeting.date.getTime())
            return meeting;
        }
        let noMeeting:Meeting = {title:"ERROR", 
        date:new Date(0), duration:0};
        return noMeeting;
    }
    perform = (actions: Array<Action>) => {
        for(let i = 0; i < actions.length; i++){
            move(this.meetingList[i%this.meetingList.length],
                 actions[i], this);
        }
    }
}

export let strMeeting = (meeting:Meeting) => {
    let startHours = meeting.date.getHours() 
    let startMinutes = meeting.date.getMinutes()
    let endingMinute = startMinutes + meeting.duration;
    let endingHours = startHours + Math.floor(endingMinute/60);
    endingMinute %= 60;
    return `${meeting.title} ${startHours}:${startMinutes}-${endingHours}:${endingMinute}`
}