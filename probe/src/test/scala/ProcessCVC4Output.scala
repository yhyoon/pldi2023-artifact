object Solutions {

  lazy val solutions = scala.io.Source.fromFile("src/test/benchmarks/solutions.txt").getLines().map(line =>
    (line.substring(0,line.indexOf(' ')),line.substring(line.indexOf(' ') + 1))).toList.groupBy(_._1).toList.map(pair => (pair._1,pair._2.map(le => le._2))).toMap
}

object ProcessCVC4Output extends App{
  val file = "src/test/benchmarks/modified_benchmarks/cvc4tests_time.out" //cvc4tests.out"
  val lines = scala.io.Source.fromFile(file).getLines().toList
  val separators = -1 +:lines.zipWithIndex.filter{case (str,idx) => str.startsWith("--")}.map(_._2)
  val resultRegex = """\s*\(define-fun\s+f\s*\((\([A-Za-z0-9_\s]+\)\s*)*\)\s+[A-Za-z]+\s*(.*)\)""".r
  for (window <- separators.sliding(2)) {
    val from = window.head
    val to = window(1)
    val segment = lines.slice(from + 1, to)
    val filename = segment.head
    val time = if (segment.last.last == 's') segment.last.dropRight(1) else segment.last
    val programs = (for (l <- segment.drop(1).dropRight(1)) yield
      l match {
        case resultRegex(_,func) => func
      }).distinct

    val goldStandard = Solutions.solutions(filename.dropRight(5) + ".sl")
    println(List(
      filename,
      programs.zipWithIndex.filter{case (program,idx) =>
          goldStandard.contains(program)
      }.headOption.map(_._2).getOrElse(" "),
      time
    ).mkString(","))
  }

}
