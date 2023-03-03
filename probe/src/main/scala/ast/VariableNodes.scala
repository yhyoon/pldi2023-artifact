package ast

abstract class VariableNode[T](contexts: List[Map[String,Any]]) extends ASTNode {
  override val height: Int = 0
  val terms = 1
  val name: String
  val values: List[T] = contexts.map{ context =>
    context(name).asInstanceOf[T]}.toList
  override lazy val code: String = name
  override val children: Iterable[ASTNode] = Iterable.empty

  def includes(varName: String): Boolean = name == varName
}

class StringVariable(val name: String, contexts: List[Map[String,Any]]) extends VariableNode[String](contexts) with StringNode

case class IntVariable(val name: String, contexts: List[Map[String,Any]]) extends VariableNode[Int](contexts) with IntNode

case class BoolVariable(val name: String, contexts: List[Map[String,Any]]) extends VariableNode[Boolean](contexts) with BoolNode

case class BVVariable(val name: String, contexts: List[Map[String,Any]]) extends VariableNode[Long](contexts) with BVNode