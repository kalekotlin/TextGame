class Tile(glyph: Char, enableCollision: Boolean) {

    val glyph: Char = glyph

    val enableCollision: Boolean = enableCollision

}

class Level(level: Array<Tile>, val x: Int, val y: Int) {

    val level: Array<Tile> = level
    val xLimit: Int = x
    val yLimit: Int = y

    fun printLevel() {
        var c = 0
        for (i in 0..level.size-1) {
            if (c == x) { 
                print("\n")
                c = 0
            }
            print(" ${level[i].glyph} ")
            c++ 
        }
    }

}

fun main() {
    val grass = Tile('.', false)
    val water = Tile('~', true)
    val mountain = Tile('^', true)

    val levelArray = arrayOf(
        mountain, mountain, mountain, water, mountain,
        mountain, grass, grass, water, mountain,
        mountain, grass, grass, water, water,
        grass, grass, grass, water, water,
        grass, grass, grass, grass, water
    )

    val level = Level(levelArray, 5, 5)
    level.printLevel()
}