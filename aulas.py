from mip import *
import io, time
from pacotePadrao import *

time_inicio = time.time()

arquivoInicial = "aulas.in"
campos_arquivoInicial = ["Pasta alunos", "Pasta curriculos", "Pasta dados", "Pasta Solução", "Configurações saída","Configurações modelo", "Lista entradas"]
tipos_arquivoInicial = [["Pasta alunos", "pasta"], ["Pasta curriculos", "pasta"], ["Pasta dados", "pasta"], ["Pasta Solução", "arquivo"], ["Configurações saída", "arquivo"],["Configurações modelo", "arquivo"],["Lista entradas","arquivo"]]

campos_arquivoConfiguracoes = ["TimeTag","CurrPri","CurrPref","Alunos","Fixos","Junto","TimeMax","SolucoesMax"]
tipos_arquivoConfiguracoes = [["TimeTag","BIN"],["CurrPri","BIN"],["CurrPref","BIN"],["Alunos","BIN"],["Fixos","BIN"],["Junto", "BIN"],["TimeMax","Numerico"],["SolucoesMax","Numerico"]]

campos_arquivoSaidas = ["Imprimir modelo", "Imprimir expandida"]
outConfs = [["Imprimir modelo",0], ["Imprimir expandida",1]]

nomes_arquivosDados = ["Horarios","Disciplinas","Turmas","Curriculos","CurriculosPri","Turnos","AlunosPesos","Interesse","Fixos","Dia","Hora","TurmasFixadas"]

(c, g, g, mainConfs, g) = trate(arquivoInicial, 
	[0, 3,
		":",
		"texto",
		[1, campos_arquivoInicial, 1],
		[1, tipos_arquivoInicial],
		[1, campos_arquivoInicial, "", 0]
	],
	[0, 3,
		";",
		"texto",
		[1, campos_arquivoInicial, 1],
		[1, tipos_arquivoInicial],
		[1, campos_arquivoInicial, "", 0]
	],
	0,
	0
)

if(c):
	mainConfs_pastaDados = getValue(mainConfs, "Pasta dados")
	mainConfs_pastaAlunos = getValue(mainConfs, "Pasta alunos")
	mainConfs_pastaCurriculos = getValue(mainConfs, "Pasta curriculos")
	mainConfs_pastaSolucao= getValue(mainConfs, "Pasta solução")
	mainConfs_configuracoesSaida = getValue(mainConfs, "Configurações saída")
	mainConfs_configuracoesModelo = getValue(mainConfs, "Configurações modelo")
	mainConfs_listaEntradas = getValue(mainConfs, "Lista entradas")
	
if(c):

	a = []
	e = []

	if(mainConfs_pastaCurriculos == ""):
		c = 0
		e.append("ERRO: Não foi indicado uma pasta em que os arquivos com informações sobre os currículos estão disponíveis para consulta [PASTA CURRICULOS], no arquivo ["+arquivoInicial+"]")

	if(mainConfs_pastaDados == ""):
		c = 0
		e.append("ERRO: Não foi indicado uma pasta em que os dados estão disponíveis para consulta [PASTA DADOS], no arquivo ["+arquivoInicial+"]")
		
	if(mainConfs_pastaSolucao == ""):
		c = 0
		e.append("ERRO: Não foi indicado uma pasta para ser inserida a solução [PASTA SOLUCAO], no arquivo ["+arquivoInicial+"]")
		
	if(mainConfs_configuracoesModelo == ""):
		c = 0
		e.append("ERRO: Não foi indicado um arquivo com as configurações do modelo [CONFIGURACOES MODELO], no arquivo ["+arquivoInicial+"]")
		
	if(mainConfs_listaEntradas == ""):
		c = 0
		e.append("ERRO: Não foi indicado um arquivo com a lista dos arquivos de dados [LISTA ENTRADAS], no arquivo ["+arquivoInicial+"]")
	
	imprimeArray(a)
	if(not c):
		imprimeArray(e)

if(c):
	fileName = mainConfs_configuracoesSaida
	if(fileName != ""):
		(c, g, g, outConfs, g) = trate(fileName, 
			[0, 3,
				":",
				"texto",
				[1, campos_arquivoSaidas, 1],
				[0, "BIN", 0],
				[1, campos_arquivoSaidas, "", 0]
			],
			[0, 3,
				";",
				"texto",
				[1, campos_arquivoSaidas, 1],
				[0, "BIN", 0],
				[1, campos_arquivoSaidas, 0, 0]
			],
			0,
			0
		)

	else:
		print("Vamos utilizar as configurações de saída padrão, já que não foi indicado nenhum arquivo em ["+arquivoInicial+"]")

if(c):
	
	fileName = mainConfs_configuracoesModelo
	(c, g, g, modeloConfs, g) = trate(fileName, 
		[0, 3,
			":",
			"texto",
			[1, campos_arquivoConfiguracoes, 1],
			[1, tipos_arquivoConfiguracoes],
			[1, campos_arquivoConfiguracoes, 0, 0]
		],
		[0, 3,
			";",
			"texto",
			[1, campos_arquivoConfiguracoes, 1],
			[1, tipos_arquivoConfiguracoes],
			[1, campos_arquivoConfiguracoes, 0, 0]
		],
		0,
		0
	)
	
	if(c):
		if(getValue(modeloConfs, "Alunos") and mainConfs_pastaAlunos == ""):
			c = 0
			print("ERRO: Não foi indicada uma pasta especifica contendo o interesse demonstrado pelos alunos [Pasta Alunos], no arquivo ["+arquivoInicial+"]")
	
if(c):
	
	fileName = mainConfs_listaEntradas
	(c, g, g, entradasLista, g) = trate(fileName, 
		[0, 3,
			":",
			"texto",
			[1, nomes_arquivosDados, 1],
			[0, "arquivo", mainConfs_pastaDados],
			[1, nomes_arquivosDados, "", 0]
		],
		[0, 3,
			";",
			"texto",
			[1, nomes_arquivosDados, 1],
			[0, "arquivo", mainConfs_pastaDados],
			[1, nomes_arquivosDados, "", 0]
		],
		0,
		0
	)
	
	if(c):
	
		a = []
		e = []
		
		if(getValue(entradasLista, "Horarios") == ""):
			c = 0
			e.append("Era necessário ter sido indicado um arquivo [Horarios] em "+fileName)
			
		if(getValue(entradasLista, "Disciplinas") == ""):
			c = 0
			e.append("Era necessário ter sido indicado um arquivo [Disciplinas] em "+fileName)
			
		if(getValue(entradasLista, "Turmas") == ""):
			c = 0
			e.append("Era necessário ter sido indicado um arquivo [Turmas] em "+fileName)
			
		if(getValue(entradasLista, "Curriculos") == ""):
			c = 0
			e.append("Era necessário ter sido indicado um arquivo [Curriculos] em "+fileName)
		
		if(getValue(modeloConfs, "Alunos") == 0 and getValue(entradasLista, "AlunosPesos") != ""):
			a.append("Levando em conta as configurações do modelo [Alunos = 0], foi desnecessária a indicação de um arquivo [AlunosPesos] em "+fileName)
			entradasLista = setValue(entradasLista, "AlunosPesos", "")
			
		if(getValue(modeloConfs, "CurrPri") == 1 and getValue(entradasLista, "CurriculosPri") == ""):
			a.append("Levando em conta as configurações do modelo [CurrPri = 1], era necessário ter sido indicado um arquivo [CurriculosPri] em "+fileName+". Consideraremos todos os currículos com o mesmo peso")
		if(getValue(modeloConfs, "CurrPri") == 0 and getValue(entradasLista, "CurriculosPri") != ""):
			a.append("Levando em conta as configurações do modelo [CurrPri = 0], foi desnecessária a indicação de um arquivo [CurriculosPri] em "+fileName)
			entradasLista = setValue(entradasLista, "CurriculosPri", "")
			
		if(getValue(modeloConfs, "CurrPref") == 1 and getValue(entradasLista, "Turnos") == ""):
			a.append("Levando em conta as configurações do modelo [CurrPref = 1], era necessário ter sido indicado um arquivo [Turnos] em "+fileName+". Consideraremos que os currículos podem ter aulas em qualquer horário possível")
		if(getValue(modeloConfs, "CurrPref") == 0 and getValue(entradasLista, "Turnos") != ""):
			a.append("Levando em conta as configurações do modelo [CurrPref = 0], foi desnecessária a indicação de um arquivo [Turnos] em "+fileName)
			entradasLista = setValue(entradasLista, "Turnos", "")
		
		if(getValue(modeloConfs, "Alunos") == 1 and getValue(entradasLista, "Interesse") == ""):
			a.append("Levando em conta as configurações do modelo [Alunos = 1], era necessário ter sido indicado um arquivo [Interesse] em "+fileName+". Dessa forma, é impossível levar em conta as preferências indicadas pelos alunos, seguiremos mesmo assim")
		if(getValue(modeloConfs, "Alunos") == 0 and getValue(entradasLista, "Interesse") != ""):
			a.append("Levando em conta as configurações do modelo [Alunos = 0], foi desnecessária a indicação de um arquivo [Interesse] em "+fileName)
			entradasLista = setValue(entradasLista, "Interesse", "")
		
		if(getValue(modeloConfs, "Fixos") == 1 and getValue(entradasLista, "Fixos") == ""):
			a.append("Levando em conta as configurações do modelo [Fixos = 1], era necessário ter sido indicado um arquivo [Fixos] em "+fileName+". Dessa forma, consideraremos que não há nenhum caracterizado como 'fixo'")
		if(getValue(modeloConfs, "Fixos") == 0 and getValue(entradasLista, "Fixos") != ""):
			a.append("Levando em conta as configurações do modelo [Fixos = 0], foi desnecessária a indicação de um arquivo [Fixos] em "+fileName)
			entradasLista = setValue(entradasLista, "Fixos", "")
		
		if(getValue(modeloConfs, "Junto") == 1 and getValue(entradasLista, "Dia") == "" and getValue(entradasLista, "Hora") == ""):
			a.append("Levando em conta as configurações do modelo [Junto = 1], era necessário ter sido indicado um arquivo [Dia] ou [Hora] em "+fileName+". Consideraremos [Junto = 0]")
		if(getValue(modeloConfs, "Junto") == 0 and (getValue(entradasLista, "Interesse") != "" or getValue(entradasLista, "Interesse") != "")):
			a.append("Levando em conta as configurações do modelo [Junto = 0], desconsideraremos qualquer indicação de um arquivo [Dia] ou [Hora] em "+fileName)
			entradasLista = setValue(entradasLista, "Dia", "")
			entradasLista = setValue(entradasLista, "Hora", "")
		
		a = addToMessage("Aviso:",a)
		imprimeArray(a)
		if(not c):
			e = addToMessage("ERRO:",e)
			imprimeArray(e)
		if(len(a) > 0):
			print("\n")
	
if(c):

	leituraSucesso = 1
	
	I_HorariosN = []
	I_HorariosM = []
	I_HorariosDuracao = []
	horasColetadas = 0
	I_Disciplinas = []
	I_Turmas = []
	I_Curriculos = []
	I_AlunosInteressados = []
	I_AlunosFixos = []
	
	C_DisciplinasDuracao = []
	C_RelacaoTurmasDisciplinas = []
	C_CurriculosPesos = []
	C_AlunosInteressadosCurriculos = []
	C_AlunosPesos = []
	C_TurmasPreenchidas = []
	
	R_TurmasDisciplinas = []
	R_CurriculosHorarios = []
	R_AlunosCumprir = []
	R_TurmasMesmoDia = []
	R_TurmasMesmaHora = []
	
	Caminhos_curriculos = []
	Caminhos_alunos = []
	
	TV_AlunosInteressadosSemestre = []
	
	if(getValue(modeloConfs, "TimeTag")):
		fileName = getValue(entradasLista, "Horarios")
		if(fileName != ""):
			(c, I_HorariosN, g, I_HorariosM, g) = trate(fileName,
				[0, 3,
					":",
					"texto",
					[
						0
					],
					[0,  "intervalod", ""],
					[0],
					[0]
				],
				[0, 3,
					";",
					"texto",
					[
						0
					],
					[0,  "intervalod", ""],
					[0],
					[0]
				],
				0,
				0
			)
			if(not c):
				leituraSucesso = c
			else:
				horasColetadas = 1
				for i in range(len(I_HorariosM)):
					if(I_HorariosM[i][0] < I_HorariosM[i][1]):
						I_HorariosDuracao.append(I_HorariosM[i][1] - I_HorariosM[i][0])
					else:
						I_HorariosDuracao.append(24*60*7 - 2 - I_HorariosM[i][0] + I_HorariosM[i][1])
	
	else:
		fileName = getValue(entradasLista, "Horarios")
		if(fileName != ""):
			(c, I_HorariosM, g) = trate(fileName, 
				[0, 4,
					"intervalod"
				],
				[0, 4,
					"intervalod"
				],
				0,
				0
			)
			if(not c):
				leituraSucesso = c
			else:
				horasColetadas = 2
	
	fileName = getValue(entradasLista, "Disciplinas")
	if(fileName != ""):
		(c, I_Disciplinas, g, C_DisciplinasDuracao, g) = trate(fileName, 
			[0, 3,
				":",
				"texto",
				[0, 0, 0],
				[0, "Numerico", 0],
				[0, 0, 0, 0]
			],
			[0, 3,
				";",
				"texto",
				[0, 0, 0],
				[0, "Numerico", ""],
				[0, 0, 0, 0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
		else:
			C_DisciplinasDuracao = colide(I_Disciplinas, C_DisciplinasDuracao) #É necessário pois não foi indicado nada em fill // Não era possível o fazer
			
	fileName = getValue(entradasLista, "Turmas")
	if(fileName != "" and I_Disciplinas):
		(c, I_Turmas, g, C_RelacaoTurmasDisciplinas, g) = trate(fileName, 
			[0, 3,
				":",
				"texto",
				[
					[
						0
					],
					[
						1,
						I_Disciplinas,
						1
					]
				],
				[0, "texto", 0],
				[0]
			],
			[0, 3,
				";",
				"texto",
				[
					[
						0
					],
					[
						1,
						I_Disciplinas,
						1
					]
				],
				[0, "texto", 0],
				[0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
		else:
			for i in range(len(I_Turmas)):
				R_TurmasDisciplinas.append([])
				for j in range(len(I_Disciplinas)):
					R_TurmasDisciplinas[-1].append(0)
			for i in range(len(C_RelacaoTurmasDisciplinas)):
				R_TurmasDisciplinas[i][I_Disciplinas.index(C_RelacaoTurmasDisciplinas[i])] = 1
	
	fileName = getValue(entradasLista, "Curriculos")
	if(fileName != ""):
		(c, I_Curriculos, g, Caminhos_curriculos, g) = trate(fileName, 
			[0, 3,
				":",
				"texto",
				[0],
				[0, "arquivo", mainConfs_pastaCurriculos],
				[0]
			],
			[0, 3,
				";",
				"texto",
				[0],
				[0, "arquivo", mainConfs_pastaCurriculos],
				[0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
		else:
			for i in range(len(I_Curriculos)):
				C_CurriculosPesos.append([I_Curriculos[i],1])
	
	fileName = getValue(entradasLista, "CurriculosPri")
	if(fileName != "" and I_Curriculos):
		(c, g, g, C_CurriculosPesos, g) = trate(fileName, 
			[0, 3,
				":",
				"texto",
				[
					1,
					I_Curriculos,
					1
				],
				[0, "Numerico", 0],
				[1, I_Curriculos, 1, 0]
			],
			[0, 3,
				";",
				"texto",
				[
					1,
					I_Curriculos,
					1
				],
				[0, "Numerico", 0],
				[1, I_Curriculos, 1, 0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
	
	fileName = getValue(entradasLista, "Turnos")
	if(fileName != "" and I_Curriculos and horasColetadas):
		(c, g, turnos, chapaTurnos, g) = trate(fileName,
			[0, 1,
				[":", ";"],
				"texto",
				[
					[
						1,
						I_Curriculos,
						1
					],
					[
						0
					],
				],
				"intervalod",
				[0, 1, 0],
				[I_Curriculos, 0, 1, 0]
			],
			[0, 1,
				[";", ";"],
				"texto",
				[
					[
						1,
						I_Curriculos,
						1
					],
					[
						0
					],
				],
				"intervalod",
				[0, 1, 0],
				[I_Curriculos, 0, 1, 0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
		else:
			turnosHorarios = []
			for i in range(len(turnos)):
				turnosHorarios.append([])
				for j in range(len(I_HorariosM)):
					if(I_HorariosM[j][0] >= turnos[i][0] and I_HorariosM[j][1] <= turnos[i][1]):
						turnosHorarios[-1].append(1)
					else:
						turnosHorarios[-1].append(0)
			
			for i in range(len(I_Curriculos)):
				R_CurriculosHorarios.append([])
				for j in range(len(I_HorariosM)):
					R_CurriculosHorarios[-1].append(0)
					
				for j in range(len(turnos)):
					if(chapaTurnos[i][j]):
						for k in range(len(I_HorariosM)):
							if(turnosHorarios[j][k]):
								R_CurriculosHorarios[i][k] = 1
	
	fileName = getValue(entradasLista, "Interesse")
	if(fileName != ""):
		(c, I_AlunosInteressados, Caminhos_alunos, alunosInteressadosCurriculosRecebidos, TV_AlunosInteressadosSemestre) = trate(fileName, 
			[0, 6,
				":",
				"texto",
				[0, "Arquivo", mainConfs_pastaAlunos, "texto", "", "texto", ""],
				[
					[0],
					[0],
					[1,I_Curriculos, 0],
					[0]
				]
			],
			[0, 6,
				";",
				"texto",
				[0, "Arquivo", mainConfs_pastaAlunos, "texto", "", "texto", ""],
				[
					[0],
					[0],
					[1,I_Curriculos, 0],
					[0]
				]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
			
		if(c):
			
			for i in range(len(I_AlunosInteressados)):
				for j in range(len(I_Curriculos)):
					if(alunosInteressadosCurriculosRecebidos[i] == I_Curriculos[j]):
						C_AlunosInteressadosCurriculos.append(j)
						break;
	
	fileName = getValue(entradasLista, "AlunosPesos")
	if(fileName != "" and I_AlunosInteressados):
		(c, g, g, C_AlunosPesos, g) = trate(fileName, 
			[0, 3,
				":",
				"texto",
				[
					1,
					I_AlunosInteressados,
					1
				],
				[0, "Numerico", 0],
				[1, I_AlunosInteressados, 1, 0]
			],
			[0, 3,
				";",
				"texto",
				[
					1,
					I_AlunosInteressados,
					1
				],
				[0, "Numerico", 0],
				[1, I_AlunosInteressados, 1, 0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
	else:
		if(I_AlunosInteressados):
			C_AlunosPesos = []
			for i in range(len(I_AlunosInteressados)):
				C_AlunosPesos.append([I_AlunosInteressados[i],1])
	
	fileName = getValue(entradasLista, "Fixos")
	if(fileName != "" and I_Turmas):
		(c, I_AlunosFixos, g, R_AlunosCumprir, g) = trate(fileName,
			[0, 1,
				[":", ";"],
				"texto",
				[
					[
						0
					],
					[
						1,
						I_Turmas,
						0
					],
				],
				"texto",
				[0, 1, 0],
				[0, I_Turmas, 0, 0]
			],
			[0, 1,
				[";", ";"],
				"texto",
				[
					[
						0
					],
					[
						1,
						I_Turmas,
						0
					],
				],
				"texto",
				[0, 1, 0],
				[0, I_Turmas, 0, 0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
	
	fileName = getValue(entradasLista, "Dia")
	if(fileName != "" and I_Turmas):
		(c, R_TurmasMesmoDia) = trate(fileName,
			[0, 5,
				";",
				I_Turmas,
				"texto",
				0
			],
			[0, 5,
				";",
				"texto",
				I_Turmas,
				0
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
	
	fileName = getValue(entradasLista, "Hora")
	if(fileName != "" and I_Turmas):
		(c, R_TurmasMesmaHora) = trate(fileName,
			[0, 5,
				";",
				I_Turmas,
				"texto",
				0
			],
			[0, 5,
				";",
				"texto",
				I_Turmas,
				0
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
	
	R_FixedTurmas = []
	
	fileName = getValue(entradasLista, "TurmasFixadas")
	if(fileName != "" and I_Turmas and horasColetadas):
		if(horasColetadas == 1):
			tipoHora = "texto"
			baseHora = I_HorariosN
		else:
			tipoHora = "intervalod"
			baseHora = I_HorariosM
		(c, g, receivedHours, chapaHorarios, g) = trate(fileName,
			[0, 1,
				[":", ";"],
				"texto",
				[
					[
						1,
						I_Turmas,
						0
					],
					[
						1,
						baseHora,
						0
					],
				],
				tipoHora,
				[0, 1, 0],
				[I_Turmas, baseHora, 0, 0]
			],
			[0, 1,
				[";", ";"],
				"texto",
				[
					[
						1,
						I_Turmas,
						0
					],
					[
						1,
						baseHora,
						0
					],
				],
				tipoHora,
				[0, 1, 0],
				[I_Turmas, baseHora, 0, 0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
		else:
			R_FixedTurmas = chapaHorarios
			for i in range(len(I_Turmas)):
				set = 0
				for j in range(len(I_HorariosM)):
				
					if(chapaHorarios[i][j]):
						set = 1
						
				C_TurmasPreenchidas.append(set)
	
	c = leituraSucesso
	
if(c):

	leituraSucesso = 1

	I_Subcurriculos = []
	Tri_curriculosTurmas = []
	
	for i in range(len(Caminhos_curriculos)):
		(c, subcurriculos, g, disciplinas, g) = trate(Caminhos_curriculos[i],
			[0, 1,
				[":", ";"],
				"texto",
				[
					[
						0
					],
					[
						1,
						I_Turmas,
						0
					],
				],
				"texto",
				[0, 1, 0],
				[0, I_Turmas, 0, 0]
			],
			[0, 1,
				[";", ";"],
				"texto",
				[
					[
						0
					],
					[
						1,
						I_Turmas,
						0
					],
				],
				"texto",
				[0, 1, 0],
				[0, I_Turmas, 0, 0]
			],
			0,
			0
		)
		if(not c):
			leituraSucesso = c
		else:
			I_Subcurriculos.append(subcurriculos)
			Tri_curriculosTurmas.append(disciplinas)
	
	C_AlunosInteressadosTurmas = []
	
	if(getValue(entradasLista, "Interesse") != ""):
	
		for i in range(len(Caminhos_alunos)):
			(c, upDim, g) = trate(Caminhos_alunos[i], 
				[0, 7, "texto", I_Turmas],
				[0, 7, "texto", I_Turmas],
				0,
				0
			)
			if(not c):
				leituraSucesso = c
			else:
				C_AlunosInteressadosTurmas.append(upDim)
		
	c = leituraSucesso
	
	time_coleta = time.time()
	if(time_coleta - time_inicio > 60):
		print("\nDemoramos cerca de ",int((time_coleta - time_inicio)/60)," minutos para coletarmos os dados\n")
	else:
		print("\nDemoramos cerca de ",int(time_coleta - time_inicio)," segundos para coletarmos os dados\n")
		
if(c and getValue(entradasLista, "Interesse") != ""):
	
	print("Agora estamos verificando a coerência de alguns dados e lapidando as informações fornecidas - isso pode demorar um pouco")
	
	print("0/2 etapas concluídas")
	
	a = []
	GM_AlunosInteressadosSemestre = []
	
	for i in range(len(TV_AlunosInteressadosSemestre)):
		identificado = 0
		for j in range(len(I_Subcurriculos[C_AlunosInteressadosCurriculos[i]])):
			if(I_Subcurriculos[C_AlunosInteressadosCurriculos[i]][j] == TV_AlunosInteressadosSemestre[i]):
				GM_AlunosInteressadosSemestre.append([C_AlunosInteressadosCurriculos[i],j])
				identificado = 1
		
		if(not identificado):
			a.append("No arquivo ["+getValue(entradasLista, "Interesse")+"] é indicado um subcurriculo {semestre} ["+TV_AlunosInteressadosSemestre[i]+"] que não pertence ao currículo do aluno ["+I_Curriculos[C_AlunosInteressadosCurriculos[i]]+"]")
		c = c*identificado
		
	print("0.2/2 etapas concluídas")
	R_AlunosInteressadosTurmasPesos = []
	for i in range(len(I_AlunosInteressados)):
		R_AlunosInteressadosTurmasPesos.append([])
		for j in range(len(I_Turmas)):
			R_AlunosInteressadosTurmasPesos[-1].append(0)
		
		for j in range(len(I_Turmas)):
			if(C_AlunosInteressadosTurmas[i][j]):
				R_AlunosInteressadosTurmasPesos[i][j] += 1
									
		for j in range(len(I_Turmas)):
			R_AlunosInteressadosTurmasPesos[i][j] *= C_CurriculosPesos[C_AlunosInteressadosCurriculos[i]][1]*C_AlunosPesos[i][1]
	
	print("0.6/2 etapas concluídas")
	for i in range(len(I_AlunosInteressados)):
		for j in range(len(I_Turmas)):
			if(Tri_curriculosTurmas[GM_AlunosInteressadosSemestre[i][0]][GM_AlunosInteressadosSemestre[i][1]][j]):
				R_AlunosInteressadosTurmasPesos[i][j] = 0
				
	imprimeArray(a)

if(c):
	
	print("1/2 etapas concluídas")
	
	GM_SubcurriculosTurmas = []
	
	for i in range(len(I_Curriculos)):
		GM_SubcurriculosTurmas.append([])
		for j in range(len(I_Subcurriculos[i])):
			GM_SubcurriculosTurmas[-1].append([])
			for k in range(len(I_Turmas)):
				GM_SubcurriculosTurmas[-1][-1].append(Tri_curriculosTurmas[i][j][k])
	
	GM_TurmasHorarios = []
	for i in range(len(I_Turmas)):
		GM_TurmasHorarios.append([])
		for j in range(len(I_HorariosM)):
			GM_TurmasHorarios[-1].append(1)
			for k in range(len(I_Curriculos)):
				if(R_CurriculosHorarios[k][j] < 1):
					GM_TurmasHorarios[i][j] = 0
					
	print("2/2 etapas concluídas")

if(c):

	print("Agora estamos montando o modelo - isso pode demorar um pouco")

	if(getValue(modeloConfs, "TimeMax") == 0):
		modeloConfs = setValue(modeloConfs, "TimeMax", 3600)
		print("Aviso rápido e importante: Limitamos o tempo de solução do problema para uma hora, caso queira processar mais/menos, reinicie o programa, definindo o vator no arquivo ["+mainConfs_configuracoesModelo+"]")
	if(getValue(modeloConfs, "TimeTag") == 0 and getValue(outConfs, "Imprimir expandida")):
		print("Aviso rápido e importante: Não será possível imprimir a solução expandida, pois [TimeTag = 0], caso queira, reinicie o programa, alterando o arquivo ["+mainConfs_configuracoesModelo+"]")
	
	print("0/6 etapas concluídas")
	
	modelo = Model()
	
	x = [[modelo.add_var(var_type=BINARY, name = "Se a turma ["+I_Turmas[i]+"] ocupará o horário ["+str(I_HorariosM[j])+"]") for j in range(len(I_HorariosM))] for i in range(len(I_Turmas))]
	y = [[modelo.add_var(var_type=BINARY, name = "Se a turma ["+I_Turmas[i]+"] colide com a turma ["+I_Turmas[j]+"]") for j in range(len(I_Turmas))] for i in range(len(I_Turmas))]
	subTurmY = [[[modelo.add_var(var_type=BINARY) for k in range(len(I_Turmas))] for j in range(len(I_Subcurriculos[i]))] for i in range(len(I_Curriculos))]
	print("1/8 etapas concluídas")
	
	for i in range(len(I_Turmas)):
		for j in range(len(I_Turmas)):
			if(i == j):
				modelo.add_constr(y[i][j] == 0, "A aula nunca colide consigo mesma")
			else:
				for k in range(len(I_HorariosM)):
					modelo.add_constr(y[i][j] + 1 >= x[i][k] + x[j][k], "Se um dos horários bater, obrigatoriamente as turmas ["+I_Turmas[i]+"] e ["+I_Turmas[j]+"] são consideradas sobrepostas")
					
	print("2/8 etapas concluídas")
	for i in range(len(I_Turmas)):
		duracao = 0
		for j in range(len(I_Disciplinas)):
			if(R_TurmasDisciplinas[i][j]):
				duracao = C_DisciplinasDuracao[i][1]
		
		if(not C_TurmasPreenchidas[i]):
			
			modelo.add_constr(xsum(x[i][j]*I_HorariosDuracao[j] for j in range(len(I_HorariosM))) == duracao)
			for j in range(len(I_HorariosM)):
		
				modelo.add_constr(x[i][j] <= GM_TurmasHorarios[i][j], "A aula ["+I_Turmas[i]+"] não pode ser lecionada às ["+str(I_HorariosM[j])+"] devido aos turnos dos subcurriculos curriculares")
					
		else:
			for j in range(len(I_HorariosM)):
				modelo.add_constr(x[i][j] == R_FixedTurmas[i][j], "A turma ["+I_Turmas[i]+"] tem seu horário pré-fixado")
				
	print("3/8 etapas concluídas")
	currTurmasMembros = []	# "índices"
	for i in range(len(I_Curriculos)):
		currTurmasMembros.append([])
		for j in range(len(I_Subcurriculos[i])):
			notCurrTurmasSemestres = []
			currTurmasMembros[i].append([])
			for k in range(len(I_Turmas)):
				if(GM_SubcurriculosTurmas[i][j][k] == 1):
					currTurmasMembros[i][-1].append(k)
				else:
					notCurrTurmasSemestres.append(k)
			modelo.add_constr(xsum(y[currTurmasMembros[i][j][k]][currTurmasMembros[i][j][l]] for k in range(len(currTurmasMembros[i][j])) for l in range(len(currTurmasMembros[i][j]))) == 0)
			
			for k in range(len(currTurmasMembros[i][j])):
				for l in range(len(notCurrTurmasSemestres)):
					modelo.add_constr(y[currTurmasMembros[i][j][k]][notCurrTurmasSemestres[l]] <= subTurmY[i][j][notCurrTurmasSemestres[l]])

	print("4/8 etapas concluídas")
	fixAlunosMembros = []
	for i in range(len(R_AlunosCumprir)):
		fixAlunosMembros.append([])
		for j in range(len(I_Turmas)):
			if(R_AlunosCumprir[i][j]):
				fixAlunosMembros[i].append(j)
				
			modelo.add_constr(xsum(y[fixAlunosMembros[i][j]][fixAlunosMembros[i][k]] for j in range(len(fixAlunosMembros[i])) for k in range(len(fixAlunosMembros[i]))) == 0)

	print("5/8 etapas concluídas")	
	I_AulasDia = [[],[],[],[],[],[],[]]
	I_HorariosDia = [[],[],[],[],[],[],[]]
	for i in range(len(I_HorariosM)):
		if(I_HorariosM[i][0] < 60*24*1):
			I_HorariosDia[0].append(i)
		elif(I_HorariosM[i][0] < 60*24*2):
			I_HorariosDia[1].append(i)
		elif(I_HorariosM[i][0] < 60*24*3):
			I_HorariosDia[2].append(i)
		elif(I_HorariosM[i][0] < 60*24*4):
			I_HorariosDia[3].append(i)
		elif(I_HorariosM[i][0] < 60*24*5):
			I_HorariosDia[4].append(i)
		elif(I_HorariosM[i][0] < 60*24*6):
			I_HorariosDia[5].append(i)
		else:
			I_HorariosDia[6].append(i)

	print("6/8 etapas concluídas")	
	tmda = 0
	if(R_TurmasMesmoDia):
		tmda = 1
	tmha = 0
	if(R_TurmasMesmaHora):
		tmha = 1
	for i in range(len(I_Turmas)):
		for j in range(len(I_Turmas)):
			if(tmda):
				if(R_TurmasMesmoDia[i][j]):
					print(I_Turmas[i],I_Turmas[j])
					for k in range(len(I_HorariosDia)):
						for l in range(len(I_HorariosDia[k])):
							modelo.add_constr(xsum(x[i][I_HorariosDia[k][l]]*I_HorariosDuracao[I_HorariosDia[k][l]] for l in range(len(I_HorariosDia[k]))) == xsum(x[j][I_HorariosDia[k][l]]*I_HorariosDuracao[I_HorariosDia[k][l]] for l in range(len(I_HorariosDia[k]))))
			if(tmha):
				if(R_TurmasMesmaHora[i][j]):
					for k in range(len(I_HorariosM)):
						modelo.add_constr(x[i][k] == x[j][k])
	
	print("7/8 etapas concluídas")
	modelo.objective = minimize(xsum(subTurmY[GM_AlunosInteressadosSemestre[i][0]][GM_AlunosInteressadosSemestre[i][1]][j]*R_AlunosInteressadosTurmasPesos[i][j] for i in range(len(I_AlunosInteressados)) for j in range(len(I_Turmas))))

	print("8/8 etapas concluídas")
	if(getValue(outConfs, "Imprimir modelo")):
		print("Tentaremos criar o arquivo com o modelo, caso o programa feche, provavelmente seja porque não há solução ["+mainConfs_pastaSolucao+"/modelo.mps]")
		if(modelo.write(mainConfs_pastaSolucao+"/modelo.mps")):
			print("Concluímos a criação do arquivo com modelo ["+mainConfs_pastaSolucao+"/modelo.mps]")
			
		print("Tentaremos criar o arquivo com o modelo, caso o programa feche, provavelmente seja porque não há solução ["+mainConfs_pastaSolucao+"/modelo.lp]")
		if(modelo.write(mainConfs_pastaSolucao+"/modelo.lp")):
			print("Não foi possível criar o arquivo com modelo ["+mainConfs_pastaSolucao+"/modelo.lp]")
	
	modelo.max_mip_gap = 1e-1
	modelo.integer_tol = 1e-1
	modelo.emphasis = "FEASIBILITY"
	
	time_processa = time.time()
	if(time_processa - time_coleta > 60):
		print("\nDemoramos cerca de ",int((time_processa - time_coleta)/60)," minutos para processarmos os dados\n")
	else:
		print("\nDemoramos cerca de ",int(time_processa - time_coleta)," segundos para processarmos os dados\n")
	
	if(getValue(modeloConfs, "SolucoesMax") == 0):
		situacao = modelo.optimize(max_seconds = getValue(modeloConfs, "TimeMax"))
	else:
		situacao = modelo.optimize(max_seconds = getValue(modeloConfs, "TimeMax"), max_solutions = getValue(modeloConfs, "SolucoesMax"))
	
	if(not (situacao == OptimizationStatus.OPTIMAL or situacao == OptimizationStatus.FEASIBLE)):
	
		print("Não foi possível encontrar nenhuma solução! Tente aliviar as restrições, expandir as possibilidades e aumentar os limites de processamento =)")
		
	else:
	
		if(situacao == OptimizationStatus.OPTIMAL):
		
			print("Encontramos uma solução ótima! Estamos muito felizes =)")
			
		else:
		
			print("Encontramos uma solução sub ótima, mas ainda assim estamos felizes =)")
			
		for i in range(len(I_Turmas)):
			for j in range(len(I_HorariosM)):
				if(x[i][j].x):
					print("A aula da turma ["+I_Turmas[i]+"] será lecionada às ["+minuto_paraHorario(I_HorariosM[j], 1, 0)+"]")
					
		print("Agora vamos salvar isso no arquivo ["+mainConfs_pastaSolucao+"/solucao.txt] e ["+mainConfs_pastaSolucao+"/solucao.csv]")
		
		try:
			with io.open(mainConfs_pastaSolucao+"/solucao.txt", "w+") as arquivo:
				arquivo.write("Turmas e seus horários:\n\n")
				for i in range(len(I_Turmas)):
					linha = ""
					for j in range(len(I_HorariosM)):
						if(x[i][j].x):
							arquivo.write("A aula da turma ["+I_Turmas[i]+"] será lecionada às ["+minuto_paraHorario(I_HorariosM[j], 1, 0)+"]\n")
				print("Acabamos de criar o arquivo ["+mainConfs_pastaSolucao+"/solucao.txt]")
		except:
			print("Não foi possível criar o arquivo ["+mainConfs_pastaSolucao+"/solucao.txt]")
		
		try:
			with io.open(mainConfs_pastaSolucao+"/solucao.csv", "w+") as arquivo:
				arquivo.write("Turma;;Horário da aula:\n\n")
				for i in range(len(I_Turmas)):
					for j in range(len(I_HorariosM)):
						if(x[i][j].x):
							arquivo.write(I_Turmas[i]+";;"+minuto_paraHorario(I_HorariosM[j], 1, I_HorariosM)+"\n")
				print("Acabamos de criar o arquivo ["+mainConfs_pastaSolucao+"/solucao.csv]")
		except:
			print("Não foi possível criar o arquivo ["+mainConfs_pastaSolucao+"/solucao.csv]")
		
		if(getValue(modeloConfs, "TimeTag") and getValue(outConfs, "Imprimir expandida")):
			
			print("Estamos nos preparando para salvar as soluções expandidas por dia")
			
			mensagens = ["","","","","","",""]
			I_AulasDia = [[],[],[],[],[],[],[]]
			I_HorariosDia = [[],[],[],[],[],[],[]]
			
			for i in range(len(I_HorariosM)):
				if(I_HorariosM[i][0] < 60*24*1):
					I_HorariosDia[0].append(i)
				elif(I_HorariosM[i][0] < 60*24*2):
					I_HorariosDia[1].append(i)
				elif(I_HorariosM[i][0] < 60*24*3):
					I_HorariosDia[2].append(i)
				elif(I_HorariosM[i][0] < 60*24*4):
					I_HorariosDia[3].append(i)
				elif(I_HorariosM[i][0] < 60*24*5):
					I_HorariosDia[4].append(i)
				elif(I_HorariosM[i][0] < 60*24*6):
					I_HorariosDia[5].append(i)
				else:
					I_HorariosDia[6].append(i)
					
			for dia in range(0, 7):
				if(len(I_HorariosDia[dia]) > 0):
					
					for i in range(len(I_HorariosDia[dia])):
						mensagens[dia] = mensagens[dia]+";"+minuto_paraHorario(I_HorariosM[I_HorariosDia[dia][i]], 1, 0)
					
					for i in range(len(I_Turmas)):
						mensagens[dia] = mensagens[dia]+"\n"+I_Turmas[i]
						for j in range(len(I_HorariosDia[dia])):
							if(x[i][I_HorariosDia[dia][j]].x):
								valor = "X"
							else:
								valor = ""
							mensagens[dia] = mensagens[dia]+";"+valor
					
			print("Agora vamos começar a salvar as soluções expandidas por dia")
			diasExtenso = ["a segunda","a terça","a quarta","a quinta","a sexta","o sábado","o domingo"]
			for dia in range(0, 7):
				if(len(I_HorariosDia[dia]) > 0):
					print("Agora vamos salvar a solução expandida d"+diasExtenso[dia]+" em ["+mainConfs_pastaSolucao+"/solucao_expandida_"+diasExtenso[dia][2:]+".csv]")
					try:
						with io.open(mainConfs_pastaSolucao+"/solucao_expandida_"+diasExtenso[dia][2:]+".csv", "w+") as arquivo:
							arquivo.write(mensagens[dia])
							print("Acabamos de criar o arquivo ["+mainConfs_pastaSolucao+"/solucao_expandida_"+diasExtenso[dia][2:]+".csv]")
					except:
						print("Não foi possível criar o arquivo ["+mainConfs_pastaSolucao+"/solucao_expandida_"+diasExtenso[dia][2:]+".csv]")
				
				else:
					print("Não há aulas n"+diasExtenso[dia]+", então não vamos criar um arquivo com a sulução expandida desse dia")
					
		print("O valor final da função objetiva é {}".format(modelo.objective_value))
					
time_fim = time.time()
if(time_fim - time_inicio > 60):
	print("\nDemoramos cerca de ",int((time_fim - time_inicio)/60)," minutos para finalizar o programa")
else:
	print("\nDemoramos cerca de ",int(time_fim - time_inicio)," segundos para finalizar o programa")
print("\n\nFim da execução do programa")