// Generated from SyGuS.g4 by ANTLR 4.7.2
package sygus;
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class SyGuSLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		LineComment=32, WS=33, Numeral=34, Decimal=35, BoolConst=36, HexConst=37, 
		BinConst=38, StringConst=39, Symbol=40;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
			"T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
			"T__25", "T__26", "T__27", "T__28", "T__29", "T__30", "LineComment", 
			"WS", "Numeral", "Decimal", "BoolConst", "HexConst", "BinConst", "StringConst", 
			"Symbol"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Int'", "'Bool'", "'Real'", "'('", "'BitVec'", "')'", "'exists'", 
			"'forall'", "'let'", "'grammars'", "'fwd-decls'", "'recursion'", "'check-synth'", 
			"'constraint'", "'declare-var'", "'inv-constraint'", "'set-feature'", 
			"':'", "'synth-fun'", "'synth-inv'", "'declare-datatype'", "'declare-datatypes'", 
			"'declare-sort'", "'define-fun'", "'define-sort'", "'set-info'", "'set-logic'", 
			"'set-option'", "'Constant'", "'Variable'", "'_'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "LineComment", "WS", 
			"Numeral", "Decimal", "BoolConst", "HexConst", "BinConst", "StringConst", 
			"Symbol"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public SyGuSLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "SyGuS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*\u01b7\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3"+
		"\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6"+
		"\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3"+
		"\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3"+
		"\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r"+
		"\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17"+
		"\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20"+
		"\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22"+
		"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25"+
		"\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27"+
		"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30"+
		"\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32"+
		"\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34"+
		"\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37"+
		"\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\7!\u016b\n!\f!\16"+
		"!\u016e\13!\3!\3!\3\"\6\"\u0173\n\"\r\"\16\"\u0174\3\"\3\"\3#\3#\7#\u017b"+
		"\n#\f#\16#\u017e\13#\3#\5#\u0181\n#\3$\3$\3$\7$\u0186\n$\f$\16$\u0189"+
		"\13$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u0196\n%\3&\3&\3&\3&\6&\u019c"+
		"\n&\r&\16&\u019d\3\'\3\'\3\'\3\'\6\'\u01a4\n\'\r\'\16\'\u01a5\3(\3(\7"+
		"(\u01aa\n(\f(\16(\u01ad\13(\3(\3(\3)\3)\7)\u01b3\n)\f)\16)\u01b6\13)\2"+
		"\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36"+
		";\37= ?!A\"C#E$G%I&K\'M(O)Q*\3\2\f\3\2\f\f\5\2\13\f\17\17\"\"\3\2\63;"+
		"\3\2\62;\3\2\62\62\5\2\62;CHch\3\2\62\63\3\2$$\f\2##&(,-/\61>AC\\`ac|"+
		"~~\u0080\u0080\f\2##&(,-/;>AC\\`ac|~~\u0080\u0080\2\u01c0\2\3\3\2\2\2"+
		"\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2"+
		"\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2"+
		"\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2"+
		"\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2"+
		"\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2"+
		"\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2"+
		"\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\3S\3\2\2\2\5W\3\2\2\2\7\\"+
		"\3\2\2\2\ta\3\2\2\2\13c\3\2\2\2\rj\3\2\2\2\17l\3\2\2\2\21s\3\2\2\2\23"+
		"z\3\2\2\2\25~\3\2\2\2\27\u0087\3\2\2\2\31\u0091\3\2\2\2\33\u009b\3\2\2"+
		"\2\35\u00a7\3\2\2\2\37\u00b2\3\2\2\2!\u00be\3\2\2\2#\u00cd\3\2\2\2%\u00d9"+
		"\3\2\2\2\'\u00db\3\2\2\2)\u00e5\3\2\2\2+\u00ef\3\2\2\2-\u0100\3\2\2\2"+
		"/\u0112\3\2\2\2\61\u011f\3\2\2\2\63\u012a\3\2\2\2\65\u0136\3\2\2\2\67"+
		"\u013f\3\2\2\29\u0149\3\2\2\2;\u0154\3\2\2\2=\u015d\3\2\2\2?\u0166\3\2"+
		"\2\2A\u0168\3\2\2\2C\u0172\3\2\2\2E\u0180\3\2\2\2G\u0182\3\2\2\2I\u0195"+
		"\3\2\2\2K\u0197\3\2\2\2M\u019f\3\2\2\2O\u01a7\3\2\2\2Q\u01b0\3\2\2\2S"+
		"T\7K\2\2TU\7p\2\2UV\7v\2\2V\4\3\2\2\2WX\7D\2\2XY\7q\2\2YZ\7q\2\2Z[\7n"+
		"\2\2[\6\3\2\2\2\\]\7T\2\2]^\7g\2\2^_\7c\2\2_`\7n\2\2`\b\3\2\2\2ab\7*\2"+
		"\2b\n\3\2\2\2cd\7D\2\2de\7k\2\2ef\7v\2\2fg\7X\2\2gh\7g\2\2hi\7e\2\2i\f"+
		"\3\2\2\2jk\7+\2\2k\16\3\2\2\2lm\7g\2\2mn\7z\2\2no\7k\2\2op\7u\2\2pq\7"+
		"v\2\2qr\7u\2\2r\20\3\2\2\2st\7h\2\2tu\7q\2\2uv\7t\2\2vw\7c\2\2wx\7n\2"+
		"\2xy\7n\2\2y\22\3\2\2\2z{\7n\2\2{|\7g\2\2|}\7v\2\2}\24\3\2\2\2~\177\7"+
		"i\2\2\177\u0080\7t\2\2\u0080\u0081\7c\2\2\u0081\u0082\7o\2\2\u0082\u0083"+
		"\7o\2\2\u0083\u0084\7c\2\2\u0084\u0085\7t\2\2\u0085\u0086\7u\2\2\u0086"+
		"\26\3\2\2\2\u0087\u0088\7h\2\2\u0088\u0089\7y\2\2\u0089\u008a\7f\2\2\u008a"+
		"\u008b\7/\2\2\u008b\u008c\7f\2\2\u008c\u008d\7g\2\2\u008d\u008e\7e\2\2"+
		"\u008e\u008f\7n\2\2\u008f\u0090\7u\2\2\u0090\30\3\2\2\2\u0091\u0092\7"+
		"t\2\2\u0092\u0093\7g\2\2\u0093\u0094\7e\2\2\u0094\u0095\7w\2\2\u0095\u0096"+
		"\7t\2\2\u0096\u0097\7u\2\2\u0097\u0098\7k\2\2\u0098\u0099\7q\2\2\u0099"+
		"\u009a\7p\2\2\u009a\32\3\2\2\2\u009b\u009c\7e\2\2\u009c\u009d\7j\2\2\u009d"+
		"\u009e\7g\2\2\u009e\u009f\7e\2\2\u009f\u00a0\7m\2\2\u00a0\u00a1\7/\2\2"+
		"\u00a1\u00a2\7u\2\2\u00a2\u00a3\7{\2\2\u00a3\u00a4\7p\2\2\u00a4\u00a5"+
		"\7v\2\2\u00a5\u00a6\7j\2\2\u00a6\34\3\2\2\2\u00a7\u00a8\7e\2\2\u00a8\u00a9"+
		"\7q\2\2\u00a9\u00aa\7p\2\2\u00aa\u00ab\7u\2\2\u00ab\u00ac\7v\2\2\u00ac"+
		"\u00ad\7t\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af\7k\2\2\u00af\u00b0\7p\2\2"+
		"\u00b0\u00b1\7v\2\2\u00b1\36\3\2\2\2\u00b2\u00b3\7f\2\2\u00b3\u00b4\7"+
		"g\2\2\u00b4\u00b5\7e\2\2\u00b5\u00b6\7n\2\2\u00b6\u00b7\7c\2\2\u00b7\u00b8"+
		"\7t\2\2\u00b8\u00b9\7g\2\2\u00b9\u00ba\7/\2\2\u00ba\u00bb\7x\2\2\u00bb"+
		"\u00bc\7c\2\2\u00bc\u00bd\7t\2\2\u00bd \3\2\2\2\u00be\u00bf\7k\2\2\u00bf"+
		"\u00c0\7p\2\2\u00c0\u00c1\7x\2\2\u00c1\u00c2\7/\2\2\u00c2\u00c3\7e\2\2"+
		"\u00c3\u00c4\7q\2\2\u00c4\u00c5\7p\2\2\u00c5\u00c6\7u\2\2\u00c6\u00c7"+
		"\7v\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca\7k\2\2\u00ca"+
		"\u00cb\7p\2\2\u00cb\u00cc\7v\2\2\u00cc\"\3\2\2\2\u00cd\u00ce\7u\2\2\u00ce"+
		"\u00cf\7g\2\2\u00cf\u00d0\7v\2\2\u00d0\u00d1\7/\2\2\u00d1\u00d2\7h\2\2"+
		"\u00d2\u00d3\7g\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7v\2\2\u00d5\u00d6"+
		"\7w\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7g\2\2\u00d8$\3\2\2\2\u00d9\u00da"+
		"\7<\2\2\u00da&\3\2\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7{\2\2\u00dd\u00de"+
		"\7p\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7j\2\2\u00e0\u00e1\7/\2\2\u00e1"+
		"\u00e2\7h\2\2\u00e2\u00e3\7w\2\2\u00e3\u00e4\7p\2\2\u00e4(\3\2\2\2\u00e5"+
		"\u00e6\7u\2\2\u00e6\u00e7\7{\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2"+
		"\u00e9\u00ea\7j\2\2\u00ea\u00eb\7/\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed"+
		"\7p\2\2\u00ed\u00ee\7x\2\2\u00ee*\3\2\2\2\u00ef\u00f0\7f\2\2\u00f0\u00f1"+
		"\7g\2\2\u00f1\u00f2\7e\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7c\2\2\u00f4"+
		"\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7\7/\2\2\u00f7\u00f8\7f\2\2"+
		"\u00f8\u00f9\7c\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc"+
		"\7v\2\2\u00fc\u00fd\7{\2\2\u00fd\u00fe\7r\2\2\u00fe\u00ff\7g\2\2\u00ff"+
		",\3\2\2\2\u0100\u0101\7f\2\2\u0101\u0102\7g\2\2\u0102\u0103\7e\2\2\u0103"+
		"\u0104\7n\2\2\u0104\u0105\7c\2\2\u0105\u0106\7t\2\2\u0106\u0107\7g\2\2"+
		"\u0107\u0108\7/\2\2\u0108\u0109\7f\2\2\u0109\u010a\7c\2\2\u010a\u010b"+
		"\7v\2\2\u010b\u010c\7c\2\2\u010c\u010d\7v\2\2\u010d\u010e\7{\2\2\u010e"+
		"\u010f\7r\2\2\u010f\u0110\7g\2\2\u0110\u0111\7u\2\2\u0111.\3\2\2\2\u0112"+
		"\u0113\7f\2\2\u0113\u0114\7g\2\2\u0114\u0115\7e\2\2\u0115\u0116\7n\2\2"+
		"\u0116\u0117\7c\2\2\u0117\u0118\7t\2\2\u0118\u0119\7g\2\2\u0119\u011a"+
		"\7/\2\2\u011a\u011b\7u\2\2\u011b\u011c\7q\2\2\u011c\u011d\7t\2\2\u011d"+
		"\u011e\7v\2\2\u011e\60\3\2\2\2\u011f\u0120\7f\2\2\u0120\u0121\7g\2\2\u0121"+
		"\u0122\7h\2\2\u0122\u0123\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125\7g\2\2"+
		"\u0125\u0126\7/\2\2\u0126\u0127\7h\2\2\u0127\u0128\7w\2\2\u0128\u0129"+
		"\7p\2\2\u0129\62\3\2\2\2\u012a\u012b\7f\2\2\u012b\u012c\7g\2\2\u012c\u012d"+
		"\7h\2\2\u012d\u012e\7k\2\2\u012e\u012f\7p\2\2\u012f\u0130\7g\2\2\u0130"+
		"\u0131\7/\2\2\u0131\u0132\7u\2\2\u0132\u0133\7q\2\2\u0133\u0134\7t\2\2"+
		"\u0134\u0135\7v\2\2\u0135\64\3\2\2\2\u0136\u0137\7u\2\2\u0137\u0138\7"+
		"g\2\2\u0138\u0139\7v\2\2\u0139\u013a\7/\2\2\u013a\u013b\7k\2\2\u013b\u013c"+
		"\7p\2\2\u013c\u013d\7h\2\2\u013d\u013e\7q\2\2\u013e\66\3\2\2\2\u013f\u0140"+
		"\7u\2\2\u0140\u0141\7g\2\2\u0141\u0142\7v\2\2\u0142\u0143\7/\2\2\u0143"+
		"\u0144\7n\2\2\u0144\u0145\7q\2\2\u0145\u0146\7i\2\2\u0146\u0147\7k\2\2"+
		"\u0147\u0148\7e\2\2\u01488\3\2\2\2\u0149\u014a\7u\2\2\u014a\u014b\7g\2"+
		"\2\u014b\u014c\7v\2\2\u014c\u014d\7/\2\2\u014d\u014e\7q\2\2\u014e\u014f"+
		"\7r\2\2\u014f\u0150\7v\2\2\u0150\u0151\7k\2\2\u0151\u0152\7q\2\2\u0152"+
		"\u0153\7p\2\2\u0153:\3\2\2\2\u0154\u0155\7E\2\2\u0155\u0156\7q\2\2\u0156"+
		"\u0157\7p\2\2\u0157\u0158\7u\2\2\u0158\u0159\7v\2\2\u0159\u015a\7c\2\2"+
		"\u015a\u015b\7p\2\2\u015b\u015c\7v\2\2\u015c<\3\2\2\2\u015d\u015e\7X\2"+
		"\2\u015e\u015f\7c\2\2\u015f\u0160\7t\2\2\u0160\u0161\7k\2\2\u0161\u0162"+
		"\7c\2\2\u0162\u0163\7d\2\2\u0163\u0164\7n\2\2\u0164\u0165\7g\2\2\u0165"+
		">\3\2\2\2\u0166\u0167\7a\2\2\u0167@\3\2\2\2\u0168\u016c\7=\2\2\u0169\u016b"+
		"\n\2\2\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c"+
		"\u016d\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\b!"+
		"\2\2\u0170B\3\2\2\2\u0171\u0173\t\3\2\2\u0172\u0171\3\2\2\2\u0173\u0174"+
		"\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176"+
		"\u0177\b\"\2\2\u0177D\3\2\2\2\u0178\u017c\t\4\2\2\u0179\u017b\t\5\2\2"+
		"\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d"+
		"\3\2\2\2\u017d\u0181\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0181\t\6\2\2\u0180"+
		"\u0178\3\2\2\2\u0180\u017f\3\2\2\2\u0181F\3\2\2\2\u0182\u0183\5E#\2\u0183"+
		"\u0187\7\60\2\2\u0184\u0186\7\62\2\2\u0185\u0184\3\2\2\2\u0186\u0189\3"+
		"\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2\u0189"+
		"\u0187\3\2\2\2\u018a\u018b\5E#\2\u018bH\3\2\2\2\u018c\u018d\7v\2\2\u018d"+
		"\u018e\7t\2\2\u018e\u018f\7w\2\2\u018f\u0196\7g\2\2\u0190\u0191\7h\2\2"+
		"\u0191\u0192\7c\2\2\u0192\u0193\7n\2\2\u0193\u0194\7u\2\2\u0194\u0196"+
		"\7g\2\2\u0195\u018c\3\2\2\2\u0195\u0190\3\2\2\2\u0196J\3\2\2\2\u0197\u0198"+
		"\7%\2\2\u0198\u0199\7z\2\2\u0199\u019b\3\2\2\2\u019a\u019c\t\7\2\2\u019b"+
		"\u019a\3\2\2\2\u019c\u019d\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019e\3\2"+
		"\2\2\u019eL\3\2\2\2\u019f\u01a0\7%\2\2\u01a0\u01a1\7d\2\2\u01a1\u01a3"+
		"\3\2\2\2\u01a2\u01a4\t\b\2\2\u01a3\u01a2\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5"+
		"\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6N\3\2\2\2\u01a7\u01ab\7$\2\2\u01a8"+
		"\u01aa\n\t\2\2\u01a9\u01a8\3\2\2\2\u01aa\u01ad\3\2\2\2\u01ab\u01a9\3\2"+
		"\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ae"+
		"\u01af\7$\2\2\u01afP\3\2\2\2\u01b0\u01b4\t\n\2\2\u01b1\u01b3\t\13\2\2"+
		"\u01b2\u01b1\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b5"+
		"\3\2\2\2\u01b5R\3\2\2\2\u01b6\u01b4\3\2\2\2\r\2\u016c\u0174\u017c\u0180"+
		"\u0187\u0195\u019d\u01a5\u01ab\u01b4\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}