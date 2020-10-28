class Level(level: CharArray) {

    val level: CharArray = level

}

fun main() {
    val levelArray = charArrayOf('a', 'b', 'c', 'd')
    val level = Level(levelArray)
    for (c in level.level) {
        print(c)
    }  
}