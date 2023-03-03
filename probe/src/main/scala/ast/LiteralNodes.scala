package ast

abstract class LiteralNode[T](numContexts: Int) extends ASTNode{
  //assert(numContexts > 0)
  val height = 0
  val terms = 1
  val value: T
  val values: List[T] = List.fill(numContexts)(value)
  override val children: Iterable[ASTNode] = Iterable.empty
  def includes(varName: String): Boolean = false
}
class StringLiteral(val value: String, numContexts: Int) extends LiteralNode[String](numContexts) with StringNode{
  override lazy val code: String = '"' + value + '"' //escape?
  }

case class IntLiteral(val value: Int, numContexts: Int) extends LiteralNode[Int](numContexts) with IntNode{
  override lazy val code: String = value.toString
  }

case class BoolLiteral(val value: Boolean, numContexts: Int) extends LiteralNode[Boolean](numContexts) with BoolNode {
  override lazy val code: String = value.toString
  }

case class BVLiteral(val value: Long, numContexts: Int) extends LiteralNode[Long](numContexts) with BVNode {
  override lazy val code: String = f"#x$value%016x"
}