USE [ESG]
GO

/****** Object:  Table [esg].[iso_standards]    Script Date: 3/22/2025 7:29:55 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [esg].[iso_standards](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[iso_standard] [nvarchar](100) NOT NULL,
	[release_date] [nvarchar](4) NOT NULL,
	[sector] [nvarchar](100) NOT NULL,
	[esg_component] [varchar](500) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [esg].[iso_standards]  WITH CHECK ADD  CONSTRAINT [FK_metric] FOREIGN KEY([esg_component])
REFERENCES [esg].[sustainability_metrics] ([name])
GO

ALTER TABLE [esg].[iso_standards] CHECK CONSTRAINT [FK_metric]
GO

