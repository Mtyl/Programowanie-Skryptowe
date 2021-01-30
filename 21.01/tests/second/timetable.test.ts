import * as ds from "../../modules/DS"
import * as chai from 'chai';

describe('timetable', function() {
    let timetable = new ds.Timetable();
    it('putOne', function() {
        let meeting: ds.Meeting = {title:"Programowanie JS", 
        date:new Date("2020-01-01 17:30"),
        duration:90}
        let date = new Date("2020-01-01 20:30")
        chai.expect(timetable.busy(meeting.date)).equal(false);
        chai.expect(timetable.canBeTransferredTo(meeting.date)).equal(true);

        chai.expect(timetable.busy(date)).equal(false);
        chai.expect(timetable.canBeTransferredTo(date)).equal(false);
        
        timetable.put(meeting);
        chai.expect(timetable.busy(meeting.date)).equal(true);
        chai.expect(timetable.canBeTransferredTo(meeting.date)).equal(false);
        
    });
    it('putMany', function(){
        let meetings: ds.Meeting[] = [{title:"Programowanie JAVA", 
        date:new Date("2020-01-01 16:00"),
        duration:90}, {title:"Spotkanie z AVG", 
        date:new Date("2020-01-01 19:00"),
        duration:60}, {title:"BHP", 
        date:new Date("2020-01-01 15:30"),
        duration:30}];
        for(let meeting of meetings){
            chai.expect(timetable.busy(meeting.date, 
                meeting.duration)).equal(false);
            chai.expect(timetable.canBeTransferredTo(meeting.date,
                meeting.duration)).equal(true);
            timetable.put(meeting);
            chai.expect(timetable.busy(meeting.date, 
                meeting.duration)).equal(true);
            chai.expect(timetable.canBeTransferredTo(meeting.date,
                meeting.duration)).equal(false);
        }
    });
    it('perform', function(){
        let actions:ds.Action[] = [ds.Action.DAY_LATER, 
            ds.Action.HOUR_LATER, ds.Action.DAY_EARLIER,
            ds.Action.HOUR_EARLIER];
        timetable.perform(actions);
        let dates:Date[] = [new Date("2020-01-02 17:30"),
        new Date("2020-01-01 17:00"), new Date("2019-12-31 19:00"),
        new Date("2020-01-01 14:30")];
        for(let date of dates){
            let meeting = timetable.get(date);
            chai.expect(meeting.title).not.equal("ERROR");
        }
    })
  });