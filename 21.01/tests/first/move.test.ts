import * as ds from "../../modules/DS"
import * as chai from 'chai';

describe('meeting', function() {
    it('move', function() {
        let meeting: ds.Meeting = {title:"Programowanie", 
        date:new Date("2020-01-01 17:30"),
        duration:90}
        ds.move(meeting, ds.Action.HOUR_LATER)
        chai.expect(meeting.date.getHours()).equal(18);
        ds.move(meeting, ds.Action.HOUR_LATER)
        chai.expect(meeting.date.getHours()).equal(18);
        chai.expect(meeting.date.getMonth()).equal(0);
        ds.move(meeting, ds.Action.DAY_EARLIER)
        chai.expect(meeting.date.getMonth()).equal(11);
    }); 
  });