## Tubling windows

* series of fixed sized non overlapping windows.

* every event is part of one window and only one window.

This is stateless aggregation / transformation because each window has nothing to do with what happened in the previous window.

## Watermarking

* event_timestamp: when did the event occur in reality; usually part of the payload

* publish_timestamp: when did the message arrive at your pubsub topic. 

spark maintains something called the state store which is a record of each window and what is contained therein.

A watermark is a timeperiod after which a window will be removed from the state store.  Therefore late arriving data that arrives past the watermark period will not be included, but if it arrives within that period it will be included.

 ## Sliding Windows

* fixed duration windows that allow overlapping

* the window of data moves forward over time based on the sliding interval.  This allows for continuous analysis of the data stream and helps detect patterns and trends over time.
