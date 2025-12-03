import kotlinx.coroutines.*
import java.time.Duration
import kotlin.system.exitProcess

fun formatTime(seconds: Int): String {
    val d = Duration.ofSeconds(seconds.toLong())
    val mm = d.toMinutes() % 60
    val ss = d.seconds % 60
    return "%02d:%02d".format(mm, ss)
}

suspend fun countdown(seconds: Int, label: String) {
    repeat(seconds) { i ->
        val left = seconds - i
        print("\r$label ${formatTime(left)} ")
        System.out.flush()
        delay(1000)
    }
    println("\r$label ${formatTime(0)} ✅       ")
}

fun parseIntArg(args: Array<String>, name: String, default: Int): Int {
    val idx = args.indexOfFirst { it == "--$name" }
    return if (idx >= 0 && idx + 1 < args.size) args[idx + 1].toIntOrNull() ?: default else default
}

fun printUsage() {
    println("Pomodoro Kotlin — usage:")
    println("  --work <minutes>    work duration (default 25)")
    println("  --break <minutes>   break duration (default 5)")
    println("  --cycles <n>        number of cycles (default 4)")
    println("  --short             run one short cycle (runs once)")
}

fun main(args: Array<String>) = runBlocking {
    if (args.contains("--help")) { printUsage(); return@runBlocking }
    val workMin = parseIntArg(args, "work", 25)
    val breakMin = parseIntArg(args, "break", 5)
    val cycles = parseIntArg(args, "cycles", 4)
    val single = args.contains("--short")
    if (workMin <= 0 || breakMin <= 0 || cycles <= 0) {
        println("Durations and cycles must be positive integers."); exitProcess(1)
    }
    val totalCycles = if (single) 1 else cycles
    println("Starting Pomodoro: work=$workMin min, break=$breakMin min, cycles=$totalCycles")
    for (c in 1..totalCycles) {
        println("\nCycle $c/$totalCycles — Focus!")
        countdown(workMin * 60, "Work:")
        if (c == totalCycles) break
        println("Break time — relax")
        countdown(breakMin * 60, "Break:")
    }
    println("\nAll done! Great job. 🎉")
}
