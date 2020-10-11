// Return one of the days of the week, which are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"

function getDayName(dateString) {
    let dayName;
    let date = String(new Date(dateString))

    let weekDay = date.slice(0, 3)
    switch(weekDay) {
        case 'Sun':
            dayName = 'Sunday'
            break
        case 'Mon':
            dayName = 'Monday'
            break
        case 'Tue':
            dayName = 'Tuesday'
            break
        case 'Wed':
            dayName = 'Wednesday'
            break
        case 'Thu':
            dayName = 'Thursday'
            break
        case 'Fri':
            dayName = 'Friday'
            break
        case 'Sat':
            dayName = 'Saturday'
            break
        default:
            break
    }
    
    return dayName;
}

console.log(getDayName('10/11/2009'))
console.log(getDayName('11/10/2010'))